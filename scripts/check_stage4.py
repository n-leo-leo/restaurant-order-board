"""Validate the published stage 4 chain. Run after both strict MkDocs builds.

python scripts/check_stage4.py /tmp/restaurant-stage4-public /tmp/restaurant-stage4-draft
Includes all stage 3 contract, archive, SVG and rendered-link checks.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'docs/project/published'
AC = re.compile(r'AC-\d{2}\.\d+')
US = re.compile(r'US-\d{2}')
TASK = re.compile(r'T-(?:\d{2}[AB]|N\d{2})')
TC = re.compile(r'TC-[MNR]\d{2}')


def ids(pattern, text):
    return set(pattern.findall(text))


def unique(items, label):
    assert len(items) == len(set(items)), ('Duplicate definition', label, items)
    return set(items)


def heading_blocks(text, prefix):
    parts = re.split(r'(?=^## ' + prefix + r')', text, flags=re.M)[1:]
    names = [re.match(r'## (\S+)', part)[1] for part in parts]
    unique(names, prefix)
    return dict(zip(names, parts))


stories = {}
for line in (P / '02_requirements/user-stories.md').read_text().splitlines():
    if re.match(r'^\| US-\d+', line):
        cells = line.split('|')
        uid = cells[1].strip()
        assert uid not in stories
        stories[uid] = {'release': 'MVP' if 'MVP' in cells[3] else 'R1',
                        'bt': set(re.findall(r'БТ-\d+', cells[4]))}
assert len(stories) == 35
acs = heading_blocks((P / '06_decomposition/acceptance-criteria.md').read_text(), 'AC-')
assert len(acs) == 46
for aid, block in acs.items():
    assert ids(US, block) <= stories.keys() and ids(US, block)
    assert all(f'**{word}:**' in block for word in ['Given', 'When', 'Then']), aid
    assert '{#' + aid.lower().replace('.', '-') + '}' in block

tasks = {}
for line in (P / '06_decomposition/tasks.md').read_text().splitlines():
    if not re.match(r'^\| <a id="t-', line):
        continue
    cells = [c.strip() for c in line.split('|')[1:-1]]
    tid = TASK.search(cells[0])[0]
    assert tid not in tasks
    if tid.startswith('T-N'):
        _, release, scope, nfr, result, deps, tests = cells
    else:
        _, scope, result, deps = cells
        release = stories[next(iter(ids(US, scope)))]['release']
    assert len(result) >= 35 and ids(AC, scope), tid
    assert ids(AC, scope) <= acs.keys() and ids(US, scope) <= stories.keys(), tid
    for aid in ids(AC, scope):
        assert ids(US, scope) & ids(US, acs[aid]), (tid, aid)
    tasks[tid] = dict(ac=ids(AC, scope), us=ids(US, scope), deps=ids(TASK, deps), release=release)
assert len(tasks) == 78
# Check the complete dependency graph, including forward references.
done, visiting = set(), set()


def visit(tid):
    assert tid in tasks, ('Unknown dependency', tid)
    assert tid not in visiting, ('Dependency cycle', tid)
    if tid in done:
        return
    visiting.add(tid)
    for dep in tasks[tid]['deps']:
        assert not (tasks[tid]['release'] == 'MVP' and tasks[dep]['release'] == 'R1'), (tid, dep)
        visit(dep)
    visiting.remove(tid)
    done.add(tid)


for tid in tasks:
    visit(tid)
full = heading_blocks((P / '07_testing/test-cases-mvp.md').read_text(), 'TC-')
assert len(full) == 61, len(full)
tests = {}
for test, block in full.items():
    assert re.fullmatch(r'TC-[MN]\d{2}', test)
    assert all(v in block for v in ['Приоритет:', '**Предусловия:**', '**Данные:**',
                                   '| Действие | Ожидаемый результат |', 'Задачи:']), test
    steps = re.findall(r'^\| (\d+) \| (.+?) \| (.+?) \|$', block, re.M)
    assert steps and [int(x[0]) for x in steps] == list(range(1, len(steps)+1)), test
    assert all(len(a) > 10 and len(b) > 20 for _, a, b in steps), test
    tests[test] = dict(ac=ids(AC, block), tasks=ids(TASK, block), release='MVP')
r1 = (P / '07_testing/test-cases-r1.md').read_text()
for line in r1.splitlines():
    if not re.match(r'^\| <a id="tc-r', line):
        continue
    cells = line.split('|')
    test = TC.search(cells[1])[0]
    assert test not in tests
    assert len(cells[2]) > 35 and ids(US, cells[3]) and ids(AC, cells[4]), test
    tests[test] = dict(ac=ids(AC, cells[4]), tasks=ids(TASK, cells[5]), release='R1')
assert len(tests) == 114, len(tests)
for test, data in tests.items():
    assert data['ac'] and data['ac'] <= acs.keys(), test
    assert data['tasks'] and data['tasks'] <= tasks.keys(), test
    assert all(tasks[t]['ac'] & data['ac'] for t in data['tasks']), test
    assert all(tasks[t]['release'] == data['release'] for t in data['tasks']), test
for tid, data in tasks.items():
    assert any(tid in test['tasks'] for test in tests.values()), ('Untested task', tid)
for uid in stories:
    assert any(uid in ids(US, a) for a in acs.values()), ('Story without AC', uid)
    assert any(uid in t['us'] for t in tasks.values()), ('Story without task', uid)

trace = (P / '08_traceability.md').read_text()
chain = trace.split('## БТ → US → AC → задачи → тест-кейсы')[1].split('\n## ')[0]
rows = [line.split('|')[1:-1] for line in chain.splitlines() if line.startswith('| БТ-')]
assert len(rows) == 46
seen = []
for bt, us, ac, task, api, test in rows:
    aid = next(iter(ids(AC, ac)))
    seen.append(aid)
    assert ids(US, us) == ids(US, acs[aid]), aid
    assert set(re.findall(r'БТ-\d+', bt)) == set().union(*(stories[u]['bt'] for u in ids(US, us))), aid
    tids, tcids = ids(TASK, task), ids(TC, test)
    assert tids and tids <= tasks.keys() and tcids and tcids <= tests.keys(), aid
    assert all(aid in tasks[t]['ac'] for t in tids), aid
    assert all(aid in tests[t]['ac'] for t in tcids), aid
    expected_tasks = {t for t, v in tasks.items() if aid in v['ac']}
    expected_tests = {t for t, v in tests.items() if aid in v['ac']}
    assert tids == expected_tasks, ('Incomplete task chain', aid, tids ^ expected_tasks)
    assert tcids == expected_tests, ('Incomplete test chain', aid, tcids ^ expected_tests)
    assert api.strip(), ('Missing API or external interface', aid)
assert unique(seen, 'Matrix AC') == acs.keys()
# Every NFR has a concrete task and check in its own mapping.
nfrows = [l.split('|')[1:-1] for l in trace.split('## НФТ → задачи → проверки', 1)[1].splitlines() if re.match(r'^\| НФТ-\d{2} \|', l)]
assert len(nfrows) == 20
assert unique([row[0].strip() for row in nfrows], 'NFR mapping') == {f'НФТ-{i:02}' for i in range(1, 21)}
for nfr, task, test in nfrows:
    assert ids(TASK, task) and ids(TASK, task) <= tasks.keys(), nfr
    assert ids(TC, test) and ids(TC, test) <= tests.keys(), nfr
# Cross-check the shared task test column against the canonical case definitions.
for line in (P / '06_decomposition/tasks.md').read_text().splitlines():
    if re.match(r'^\| <a id="t-n', line):
        cells = line.split('|')
        tid = TASK.search(cells[1])[0]
        for test in ids(TC, cells[-2]):
            assert test in tests and tid in tests[test]['tasks'], ('Nonreciprocal shared task', tid, test)
assert unique([row[0].strip() for row in nfrows], 'NFR mapping') == {f'НФТ-{i:02}' for i in range(1, 21)}
for nfr, task, test in nfrows:
    nr = nfr.strip()
    assert any(nr in full.get(t, '') or any(t in row and nr in row for row in r1.splitlines())
               for t in ids(TC, test)), ('NFR check lacks requirement', nr)
for path in ['06_decomposition', '07_testing', '08_traceability.md']:
    assert not (ROOT / 'docs/project/documentation' / path).exists(), path
for file in [P / '08_traceability.md', *(P / '06_decomposition').glob('*.md'), *(P / '07_testing').glob('*.md')]:
    assert not re.search(r'Заполнить|Этап 4 остается незавершенным|Источник: ДЗ', file.read_text()), file
    unique(re.findall(r'(?:\{#([^}]+)\}|<a id="([^"]+)")', file.read_text()), file)
# All explicit references in the finished sections resolve to canonical definitions.
finished = [P / '08_traceability.md', *(P / '06_decomposition').glob('*.md'), *(P / '07_testing').glob('*.md')]
for file in finished:
    content = file.read_text()
    assert ids(AC, content) <= acs.keys(), ('Unknown AC', file)
    assert ids(US, content) <= stories.keys(), ('Unknown US', file)
    assert ids(TASK, content) <= tasks.keys(), ('Unknown task', file)
    assert ids(TC, content) <= tests.keys(), ('Unknown case', file)
checklist = (P / '07_testing/checklist.md').read_text()
check_ids = re.findall(r'^\| (CL-\d+) \|', checklist, re.M)
assert unique(check_ids, 'Checklist') == {f'CL-{i:02}' for i in range(1, 25)}
assert 'не выполнялись' in (P / '07_testing/test-cases-mvp.md').read_text()
assert 'не выполнялись' in r1
subprocess.run([sys.executable, str(ROOT / 'scripts/check_stage3.py'), *sys.argv[1:]], check=True)
print(f'PASS stage 4: {len(stories)} US, {len(acs)} AC, {len(tasks)} tasks, '
      f'{len(full)} full MVP cases, {len(tests)-len(full)} R1 titles, 20 NFR; complete bidirectional trace and acyclic dependencies')

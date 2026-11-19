/* Check representative clickable prototype flows locally, without any backend. */
const assert=require('node:assert/strict'),path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
(async()=>{const browser=await chromium.launch({headless:true,channel:'chrome'});try{
 const page=await browser.newPage({viewport:{width:1600,height:1500},locale:'ru-RU'});
 const url=pathToFileURL(path.resolve(__dirname,'../docs/project/published/assets/prototype/index.html'));
 const open=async(screen,state='default')=>{const u=new URL(url);u.searchParams.set('screen',screen);u.searchParams.set('state',state);await page.goto(u.href);};
 const click=async(action)=>page.locator(`[data-action="${action}"]`).first().click();
 const state=()=>page.evaluate(()=>({screen:prototypeApp.state.screen,state:prototypeApp.state.state,cart:prototypeApp.state.cart}));
 const text=()=>page.locator('#screen').innerText();
 await open('K-01');await click('add:classic');await click('go:K-03');await click('service');await click('chooseService:takeaway');await click('prepare');await click('pay');assert.equal((await state()).screen,'K-04');assert.match(await text(),/648/);
 assert.equal((await state()).state,'holding');assert.equal(await page.locator('[data-action="resultPaid"]').count(),0);
 await click('go:K-04:holdExpired');assert.match(await text(),/Оплата не началась/);await click('go:K-03');await click('prepare');await click('pay');await click('go:K-04');
 await click('resultUnknown');assert.equal((await state()).state,'unknown');assert.equal(await page.locator('#screen [data-action="pay"],#screen [data-action="reset"]').count(),0);
 await click('resultPaid');assert.equal((await state()).screen,'K-05');assert.match(await text(),/648/);await click('reset');assert.equal((await state()).cart.length,0);console.log('PASS kiosk: quantities, type, server-calculation fixture, unknown payment, late success, clean next session');
 await open('K-01');await click('category:Гарниры');await click('dish:fries');assert.match(await text(),/Картофель в панировке/);assert.doesNotMatch(await text(),/Дополнить заказ/);console.log('PASS product card: selected item composition and burger-only upsell');
 await open('K-03','changed');await click('pay');assert.match(await text(),/396/);console.log('PASS changed calculation: explicit agreement preserves the new amount through payment');
 await open('S-02');assert.equal(await page.locator('[data-action="reprint"]').isDisabled(),true);await click('verify');await page.locator('[name="evidenceChecked"]').check();await click('confirmVerification');await click('reprint');assert.equal((await state()).state,'reprinted');assert.match(await text(),/Киоск 3/);
 await click('go:S-01');await click('findMvp');assert.match(await text(),/Место печати копии — Киоск 3/);await click('resolve');assert.equal((await state()).state,'resolved');console.log('PASS manager: verification before reprint, same public order, resolution after documents');
 await open('S-02');await click('impossibility');await page.locator('[name="cancelComment"]').fill('Приготовление невозможно по подтвержденной проблеме');await click('confirmCancellation');assert.equal((await state()).state,'cancelled');assert.match(await text(),/требуется/);await click('externalRefund');await page.locator('[name="refundReference"]').fill('RF-DEMO-042');await click('registerRefund');assert.equal((await state()).state,'refundPending');await click('moneyConfirmed');assert.match(await text(),/Деньги возвращены. Чек возврата на сверке/);assert.equal(await page.locator('[data-action="externalRefund"]').isDisabled(),true);await click('refundConfirmed');assert.equal((await state()).state,'refundConfirmed');console.log('PASS MVP refund: cancellation, external reference and confirmation are separate steps');
 await open('R-04','detail');await click('r1Cancel');await page.locator('[name="cancelComment"]').fill('Просьба гостя до начала приготовления');await click('confirmCancellation');
 assert.equal((await state()).state,'cancelPending');assert.ok(await page.locator('[data-action="r1Refund"]').isDisabled());
 await click('go:R-04:cancelled');await click('r1Refund');await click('registerRefund');assert.equal((await state()).state,'refundPending');assert.equal(await page.locator('[data-action="r1Refund"]').isDisabled(),true);console.log('PASS R1: full refund starts separately and cannot be started again while pending');
 await open('R-04','cancelPending');await click('go:R-04:cancelTooLate');assert.match(await text(),/Просьба об отмене отклонена/);assert.ok(await page.locator('[data-action="r1Refund"]').isDisabled());
 for(const [event,reason] of [['confirmedProblem','Подтвержденная проблема'],['confirmedImpossible','Невозможность выполнения']]){
  await open('R-04');await click('r1Detail:042');await click('r1Cancel');
  await page.locator('[name="cancelComment"]').fill('Гость просит отменить заказ');
  await click('confirmCancellation');await click('go:R-04:cancelTooLate');await click('go:R-04');
  assert.match(await page.locator('tr').filter({hasText:'042'}).innerText(),/Готовится/);
  await click('r1Detail:042');assert.match(await text(),/Состав заказа/);assert.match(await text(),/Просьба об отмене отклонена/);
  assert.ok(await page.locator('[data-action="r1Cancel"]').isDisabled());
  assert.ok(await page.locator('[data-action="r1Refund"]').isDisabled());
  await click(event);await click('go:R-04');await click('r1Detail:041');
  assert.ok(await page.locator('[data-action="r1Cancel"]').isDisabled());
  await click('go:R-04');await click('r1Detail:042');await click('r1Cancel');
  assert.deepEqual(await page.locator('[name="cancelReason"] option').allTextContents(),[reason]);
  await page.locator('[name="cancelComment"]').fill(reason);await click('confirmCancellation');
  await click('go:R-04');await click('r1Detail:042');assert.equal((await state()).state,'cancelled');
  assert.ok(await page.locator('[data-action="r1Refund"]').isEnabled());
 }
 console.log('PASS R-04: refusal preserves preparing order; a separate confirmed ground enables cancellation for that order');
 await open('S-01','accepted');await click('go:S-01:deliveryReconciled');assert.match(await text(),/65 секунд/);
 await open('S-01');await click('go:S-02:paymentUnknown');assert.match(await text(),/Публичный номер еще не присвоен/);assert.equal(await page.locator('#screen [data-action="reprint"],#screen [data-action="impossibility"]').count(),0);await open('R-04');await click('r1Detail:041');assert.match(await text(),/Заказ 041/);assert.equal(await page.locator('[data-action="r1Cancel"]').isDisabled(),true);console.log('PASS staff context: unknown payment has no public number; selected preparing order cannot be cancelled on request');
 await open('S-04');await click('stopSales');await click('confirmStop');assert.equal((await state()).state,'stopped');await click('resumeSales');assert.equal((await state()).state,'default');await open('S-04','technical');assert.equal(await page.locator('[data-action="resumeSales"]').isDisabled(),true);console.log('PASS sales: explicit stop and resume, failed readiness blocks resume');
 await open('R-03');await click('cancelCash');await click('confirmCashReturn');assert.equal((await state()).state,'returnUnknown');assert.equal(await page.locator('#screen [data-action="pay"],#screen [data-action="reset"]').count(),0);await click('cashReturned');assert.equal((await state()).screen,'K-03');console.log('PASS cash: unknown return blocks the next guest action until confirmation');
 await open('R-01','register');const originalCart=(await state()).cart;await page.locator('[name="phone"]').fill('+79000000000');await page.locator('[name="guestName"]').fill('Гость');await page.locator('[name="birthDate"]').fill('1995-05-05');await click('sendCode');await page.locator('[name="sms"]').fill('123456');await click('authConfirm');assert.equal((await state()).screen,'R-02');assert.deepEqual((await state()).cart,originalCart);assert.match(await text(),/Классический бургер/);assert.match(await text(),/Картофель фри/);assert.doesNotMatch(await text(),/Большое комбо|✓ Подарок/);assert.equal(await page.locator('[name="bonus"]').getAttribute('max'),'113');await page.locator('[name="bonus"]').fill('0');await page.locator('[name="bonus"]').blur();assert.match(await text(),/К оплате деньгами\s*378/);await page.locator('[name="bonus"]').fill('114');await click('bonusPay');assert.equal((await state()).state,'default');await page.locator('[name="bonus"]').fill('100');await page.locator('[name="bonus"]').blur();await click('bonusPay');await click('methodCash');assert.equal((await state()).screen,'R-03');assert.match(await text(),/278/);assert.deepEqual((await state()).cart,originalCart);console.log('PASS loyalty: registration preserves basket; cap uses current total; invalid amount blocked; agreed amount reaches cash payment');
 await open('R-02','noBonus');assert.equal(await page.locator('[name="bonus"]').isDisabled(),true);await click('bonusPay');await click('methodCard');assert.match(await text(),/378/);
 await open('R-02','giftEligible');assert.equal(await page.locator('[name="bonus"]').getAttribute('max'),'518');assert.match(await text(),/✓ Подарок/);await page.locator('[name="bonus"]').fill('518');await page.locator('[name="bonus"]').blur();await click('bonusPay');await click('methodCard');assert.match(await text(),/1\s?210/);assert.deepEqual((await state()).cart,[{id:'classic',qty:6},{id:'fries',qty:1}]);await open('R-02','giftMissing');assert.match(await text(),/стаканы закончились/);console.log('PASS loyalty fixtures: zero balance, separate gift basket, dynamic cap and missing gift');
 await open('B-01','error');assert.doesNotMatch(await text(),/042|044|041|043/);await open('S-03','fault');await click('cellService');assert.equal((await state()).state,'fault');console.log('PASS board/cell: stale public numbers hidden; cleaning does not clear a sensor fault');
 await open('S-01');
 for(const [day,expected] of [['2026-11-15','Заказ выдан'],['2026-11-16','Киоск 2'],['2026-11-14','Заказ не найден']]){
  await open('S-01');await page.locator('[name="day"]').fill(day);await click('findMvp');assert.ok((await text()).includes(expected));
 }
 await open('S-01');await page.locator('[name="orderNumber"]').fill('42');await click('findMvp');assert.match(await text(),/Заказ не найден/);
 await open('B-02','accessUnconfirmed');assert.match(await text(),/Менеджер проверит/);assert.doesNotMatch(await text(),/Заказ получен|неявка/i);
 await open('R-02','cardOnly');assert.equal(await page.locator('[data-action="methodCash"]').count(),0);
 await open('R-02','method');await click('cashFailure');await click('methodCash');assert.equal((await state()).state,'cardOnly');await click('methodCard');assert.equal((await state()).screen,'K-04');
 await open('R-08');await page.locator('[name="reportTo"]').fill('2026-11-17');await click('makeReport');
 const days=page.locator('[name="exportDay"]');await days.selectOption({index:1});assert.equal(await page.locator('[data-action="export"]').isDisabled(),true);
 await days.selectOption({index:0});const dayId=await days.inputValue();await click('export');assert.equal(await page.evaluate(()=>prototypeApp.state.exportTradingDayId),dayId);
 await click('exportConfirmed');await click('export');assert.match(await text(),/Новых операций/);
 await click('lateSale');await click('export');assert.match(await text(),/№ 02-20261115/);await click('exportFailed');await click('export');await click('exportConfirmed');
 assert.equal((await state()).state,'supplementDone');assert.match(await text(),/53 200/);await click('export');assert.match(await text(),/Новых операций/);
 const metric=label=>page.locator('.metric').filter({hasText:label}).locator('strong').innerText();
 for(const index of [1,0]){
  await days.selectOption({index});
  assert.equal(await metric('Оплаченных заказов'),'48');assert.equal(await metric('Оплачено деньгами'),'55 200 ₽');
  assert.match(await page.locator('tr').filter({hasText:'Итого за период'}).innerText(),/53 200 ₽/);
  assert.equal((await state()).state,index===1?'default':'supplementDone');
 }
 await page.locator('[name="reportFrom"]').fill('2026-11-16');await click('makeReport');
 assert.equal(await metric('Оплаченных заказов'),'0');
 await page.locator('[name="reportFrom"]').fill('2026-11-15');await click('makeReport');
 assert.equal(await metric('Оплаченных заказов'),'48');assert.equal((await state()).state,'supplementDone');
 console.log('PASS R-08: late payment counted once across export days and period changes');
 await open('R-07');assert.match(await text(),/29,99%/);
 console.log('PASS exact day search, fiscal reconciliation, cash availability, closed day export and supply threshold');
 console.log('All prototype checks passed. These are demo UI checks, not integration tests.');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1});

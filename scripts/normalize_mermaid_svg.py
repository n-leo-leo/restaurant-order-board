"""Make exported Mermaid SVG independent of the MkDocs page theme."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / "docs/project/published/assets"
LIGHT_THEME = {
    "--md-default-bg-color": "#ffffff",
    "--md-default-fg-color--lightest": "#f1f4f8",
    "--md-default-fg-color--lighter": "#a7b3c2",
}


def normalize(source):
    root = ET.fromstring(source)
    variables = dict(LIGHT_THEME)
    variables.update(re.findall(r"(--[\w-]+):([^;]+)", root.get("style", "")))

    def resolve(match):
        key = match.group(1)
        if key not in variables:
            raise ValueError(f"Missing standalone SVG color: {key}")
        return variables[key]

    result = re.sub(r"var\((--[\w-]+)\)", resolve, source)
    if "var(" in result:
        raise ValueError("Unsupported CSS variable expression")
    ET.fromstring(result)
    return result


if __name__ == "__main__":
    # Validate the entire batch before writing any file.
    outputs = {p: normalize(p.read_text()) for p in ASSETS.glob("stage2-*.svg")}
    for file, content in outputs.items():
        if content != file.read_text():
            file.write_text(content)
    print(f"Validated {len(outputs)} standalone SVG files")

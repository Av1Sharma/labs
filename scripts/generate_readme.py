"""Refresh the generated index of Python exercises in the root README."""
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- BEGIN AUTO-GENERATED LAB INDEX -->"
END = "<!-- END AUTO-GENERATED LAB INDEX -->"


def description(path: Path) -> str:
    if path.name.startswith("test") or path.name.startswith("tests"):
        return "Course-provided test or exercise checks."
    try:
        module = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return "Python exercise or supporting script."
    docstring = ast.get_docstring(module)
    if not docstring:
        return "Python exercise or supporting script."
    sentence = next((line.strip() for line in docstring.splitlines() if line.strip()), "")
    if not sentence:
        return "Python exercise or supporting script."
    sentence = sentence.split("\n", 1)[0].strip()
    if len(sentence) > 150:
        sentence = sentence[:147].rstrip() + "..."
    return sentence.replace("`", "'")


def generated_section() -> str:
    lines = [START, "### Python exercise index", ""]
    paths = sorted(
        path for path in ROOT.rglob("*.py")
        if "__pycache__" not in path.parts and path != Path(__file__)
    )
    grouped: dict[str, list[Path]] = {}
    for path in paths:
        grouped.setdefault(path.relative_to(ROOT).parts[0], []).append(path)
    for folder, files in grouped.items():
        lines.append(f"#### `{folder}/`")
        lines.append("")
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            lines.append(f"- [`{path.name}`]({relative}) — {description(path)}")
        lines.append("")
    lines.extend([END, ""])
    return "\n".join(lines)


content = README.read_text(encoding="utf-8")
section = generated_section()
if START in content and END in content:
    before = content.split(START, 1)[0]
    after = content.split(END, 1)[1]
    content = before + section + after.lstrip("\n")
else:
    marker = "## Running a file\n"
    if marker not in content:
        raise SystemExit("README.md is missing the 'Running a file' insertion point.")
    content = content.replace(marker, section + marker, 1)

README.write_text(content, encoding="utf-8")
print("Updated the generated Python exercise index in README.md.")

import re
from pathlib import Path


def extract_local_links(text: str):
    pattern = re.compile(r"\[[^\]]*\]\((?!https?://|mailto:|#)([^)]+)\)")
    return pattern.findall(text)


def test_readme_links_exist():
    root = Path(__file__).resolve().parents[1]
    readme_path = root / "README.md"
    content = readme_path.read_text()
    for link in extract_local_links(content):
        path = root / link
        assert path.exists(), f"Missing README resource: {link}"

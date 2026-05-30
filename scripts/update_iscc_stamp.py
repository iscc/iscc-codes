#!/usr/bin/env python3
"""Update or verify the ISCC-SUM stamp shown on the license page.

The license page displays the ISCC-SUM for the documentation source tree. The
page itself is excluded via ``docs/.isccignore`` so the embedded stamp does not
invalidate its own input.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
LICENSE_PAGE = DOCS_DIR / "license.md"
ISCCIGNORE = DOCS_DIR / ".isccignore"
START = "<!-- iscc-sum:start -->"
END = "<!-- iscc-sum:end -->"
STAMP_RE = re.compile(r"ISCC:[A-Z2-7]+")


def run_iscc_sum() -> str:
    """Return the default wide ISCC-SUM for the docs tree."""
    result = subprocess.run(
        ["iscc-sum", "--tree", "docs"],
        cwd=REPO_ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    first_line = result.stdout.splitlines()[0]
    match = STAMP_RE.search(first_line)
    if not match:
        raise RuntimeError(f"Could not parse ISCC-SUM from output: {first_line!r}")
    return match.group(0)


def ensure_ignore_excludes_license() -> None:
    if not ISCCIGNORE.exists():
        raise RuntimeError("docs/.isccignore is missing")
    patterns = {
        line.strip()
        for line in ISCCIGNORE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    if "license.md" not in patterns and "/license.md" not in patterns:
        raise RuntimeError("docs/.isccignore must exclude license.md to avoid stamp self-reference")


def render_block(iscc: str) -> str:
    # Keep blank lines inside the HTML-comment markers so mdformat leaves the
    # generated block stable. The pre-commit hook runs mdformat before this
    # script, and both tools must converge without fighting each other.
    return f"""{START}

**Documentation source ISCC-SUM**: `{iscc}`

This wide ISCC-SUM identifies the documentation source tree generated with
`iscc-sum --tree docs`. The license page itself is excluded from the tree via
`docs/.isccignore` so this embedded stamp is not self-referential.

{END}"""


def update_license_page(iscc: str) -> bool:
    text = LICENSE_PAGE.read_text(encoding="utf-8")
    block = render_block(iscc)
    if START in text and END in text:
        new_text = re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            block,
            text,
            flags=re.DOTALL,
        )
    else:
        # Replace the old POC-era TITLE/ISCC block if present; otherwise insert
        # the modern stamp just below the page heading.
        old_block = re.compile(
            r"\n\*\*TITLE\*\*: ISCC - Content Codes\n\n\*\*ISCC\*\*: [^\n]+\n",
            flags=re.MULTILINE,
        )
        if old_block.search(text):
            new_text = old_block.sub("\n" + block + "\n", text)
        else:
            new_text = text.replace("# License\n", "# License\n\n" + block + "\n", 1)
    if new_text != text:
        LICENSE_PAGE.write_text(new_text, encoding="utf-8")
        return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify that the committed stamp is current")
    args = parser.parse_args(argv)

    ensure_ignore_excludes_license()
    iscc = run_iscc_sum()
    before = LICENSE_PAGE.read_text(encoding="utf-8")
    changed = update_license_page(iscc)
    if args.check and changed:
        LICENSE_PAGE.write_text(before, encoding="utf-8")
        print(
            "docs/license.md contains a stale ISCC-SUM stamp. "
            "Run `uv run --group dev python scripts/update_iscc_stamp.py`.",
            file=sys.stderr,
        )
        return 1
    if changed:
        print(f"Updated documentation ISCC-SUM stamp: {iscc}")
    else:
        print(f"Documentation ISCC-SUM stamp is current: {iscc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

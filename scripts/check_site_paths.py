#!/usr/bin/env python3
"""Check URL compatibility requirements for the iscc.codes site.

The script intentionally uses only the Python standard library so it can run in
GitHub Actions before the documentation toolchain is installed. By default it
checks source files. With ``--site-dir`` it also checks generated output.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SOURCE_PATHS = {
    "/": Path("docs/index.md"),
    "/concept/": Path("docs/concept.md"),
    "/features/": Path("docs/features.md"),
    "/license/": Path("docs/license.md"),
    "/resources/": Path("docs/resources.md"),
    "/specification/": Path("docs/specification.md"),
}

# Historical path currently handled by mkdocs-redirects.
COMPATIBILITY_PATHS = ("/implementations/",)

EXPECTED_MKDOCS_SETTINGS = {
    "site_url": "https://iscc.codes",
    "repo_name": "iscc/iscc-codes",
    "repo_url": "https://github.com/iscc/iscc-codes",
    "edit_uri": "edit/version-1.1/docs/",
}

OLD_REPOSITORY_SLUG = "iscc/iscc-specs"


def generated_index_for(site_dir: Path, url_path: str) -> Path:
    """Return the expected generated index.html file for a canonical path."""
    if url_path == "/":
        return site_dir / "index.html"
    return site_dir / url_path.strip("/") / "index.html"


def check_source_files(repo_root: Path) -> list[str]:
    """Verify that required source pages and migration notes exist."""
    errors: list[str] = []

    for url_path, source_path in REQUIRED_SOURCE_PATHS.items():
        absolute_path = repo_root / source_path
        if not absolute_path.is_file():
            errors.append(f"missing source for {url_path}: {source_path}")

    migration_notes = repo_root / "maintainers/site-migration.md"
    if not migration_notes.is_file():
        errors.append("missing maintainer migration notes: maintainers/site-migration.md")

    cname = repo_root / "docs/CNAME"
    if not cname.is_file():
        errors.append("missing custom domain file: docs/CNAME")
    elif cname.read_text(encoding="utf-8").strip() != "iscc.codes":
        errors.append("docs/CNAME must contain exactly: iscc.codes")

    mkdocs_config = repo_root / "mkdocs.yml"
    if mkdocs_config.is_file():
        mkdocs_text = mkdocs_config.read_text(encoding="utf-8")
        for key, expected_value in EXPECTED_MKDOCS_SETTINGS.items():
            setting_pattern = re.compile(
                rf"^{re.escape(key)}:\s*['\"]{re.escape(expected_value)}['\"]\s*$",
                re.MULTILINE,
            )
            if setting_pattern.search(mkdocs_text) is None:
                errors.append(f"mkdocs.yml should set {key}: {expected_value}")

        redirect_pattern = re.compile(
            r"['\"]?implementations\.md['\"]?\s*:\s*['\"]?resources\.md['\"]?"
        )
        if redirect_pattern.search(mkdocs_text) is None:
            errors.append("mkdocs.yml should preserve implementations.md -> resources.md redirect")

    old_slug_files = (
        repo_root / "README.md",
        repo_root / "mkdocs.yml",
        repo_root / "pyproject.toml",
        repo_root / "docs/resources.md",
        repo_root / "docs/specification.md",
        repo_root / "maintainers/site-migration.md",
    )
    for path in old_slug_files:
        if path.is_file() and OLD_REPOSITORY_SLUG in path.read_text(encoding="utf-8"):
            errors.append(f"old repository slug remains in {path.relative_to(repo_root)}")

    return errors


def check_generated_site(site_dir: Path) -> list[str]:
    """Verify generated output paths when a site directory is available."""
    errors: list[str] = []

    if not site_dir.is_dir():
        return [f"site directory does not exist: {site_dir}"]

    for url_path in REQUIRED_SOURCE_PATHS:
        index_file = generated_index_for(site_dir, url_path)
        if not index_file.is_file():
            errors.append(f"missing generated page for {url_path}: {index_file}")

    for url_path in COMPATIBILITY_PATHS:
        index_file = generated_index_for(site_dir, url_path)
        if not index_file.is_file():
            errors.append(f"missing generated compatibility path for {url_path}: {index_file}")

    cname = site_dir / "CNAME"
    if not cname.is_file():
        errors.append(f"missing generated custom domain file: {cname}")
    elif cname.read_text(encoding="utf-8").strip() != "iscc.codes":
        errors.append("generated CNAME must contain exactly: iscc.codes")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root to check. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        help="Optional generated site directory to check, for example 'site'.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()

    errors = check_source_files(repo_root)
    if args.site_dir is not None:
        site_dir = args.site_dir
        if not site_dir.is_absolute():
            site_dir = repo_root / site_dir
        errors.extend(check_generated_site(site_dir.resolve()))

    if errors:
        print("Site path compatibility check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Site path compatibility check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

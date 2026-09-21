"""Publish Markdown sources beside the rendered site for people and language models.

Every page under the docs directory is written to the site output as `index.md`
next to its `index.html`, which is where the theme's "Copy page" button and the
"View as Markdown" action look for it. A concatenated `llms-full.txt` in
navigation order is written to the site root.

Run after `zensical build`:

    uv run python scripts/gen_markdown_pages.py
"""

import argparse
import re
import sys
import tomllib
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)


def load_config(config_path):
    """Return the `[project]` table of a Zensical configuration file."""
    with config_path.open("rb") as fp:
        return tomllib.load(fp)["project"]


def flatten_nav(nav):
    """Return the Markdown paths of a Zensical `nav` list in reading order."""
    paths = []
    for item in nav:
        if isinstance(item, str):
            paths.append(item)
        elif isinstance(item, dict):
            for value in item.values():
                paths.extend(flatten_nav(value if isinstance(value, list) else [value]))
    return paths


def page_sources(docs_dir, custom_dir):
    """Return every Markdown page under docs, excluding the theme override directory."""
    excluded = custom_dir.resolve() if custom_dir else None
    sources = []
    for path in sorted(docs_dir.rglob("*.md")):
        if excluded and excluded in path.resolve().parents:
            continue
        sources.append(path.relative_to(docs_dir))
    return sources


def output_path(site_dir, rel_path):
    """Map a docs-relative Markdown path to its directory-URL location in the site."""
    if rel_path.name == "index.md":
        return site_dir / rel_path
    return site_dir / rel_path.with_suffix("") / "index.md"


def clean_markdown(text):
    """Strip YAML frontmatter and surrounding whitespace."""
    return FRONTMATTER_RE.sub("", text).strip() + "\n"


def ordered_sources(sources, nav):
    """Sort sources by navigation order, appending pages the nav does not mention."""
    nav_paths = [Path(p) for p in flatten_nav(nav)]
    ordered = [p for p in nav_paths if p in sources]
    ordered.extend(p for p in sources if p not in ordered)
    return ordered


def main(argv=None):
    """Write per-page Markdown files and llms-full.txt into the built site."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", default="zensical.toml", type=Path)
    parser.add_argument("--site-dir", default="site", type=Path)
    args = parser.parse_args(argv)

    project = load_config(args.config)
    root = args.config.resolve().parent
    docs_dir = root / project.get("docs_dir", "docs")
    custom_dir = project.get("theme", {}).get("custom_dir")
    custom_dir = root / custom_dir if custom_dir else None
    site_dir = args.site_dir if args.site_dir.is_absolute() else root / args.site_dir

    if not site_dir.is_dir():
        print(f"site directory not found: {site_dir} (run zensical build first)", file=sys.stderr)
        return 1

    sources = ordered_sources(page_sources(docs_dir, custom_dir), project.get("nav", []))
    full = []
    for rel_path in sources:
        text = clean_markdown((docs_dir / rel_path).read_text(encoding="utf-8"))
        target = output_path(site_dir, rel_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        full.append(text)

    (site_dir / "llms-full.txt").write_text("\n\n".join(full), encoding="utf-8")
    print(f"wrote {len(sources)} Markdown pages and llms-full.txt to {site_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

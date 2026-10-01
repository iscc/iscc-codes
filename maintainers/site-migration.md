# Site Migration Notes

This document records the public URL and deployment constraints for the
`iscc.codes` documentation site during the migration from MkDocs to Zensical.
It is intended for maintainers. The goal is continuity: existing links should
continue to work, and old entry points should either remain useful pages or
forward to the most relevant replacement.

## Current deployment

- Public site: <https://iscc.codes/>
- Custom domain: `iscc.codes`
- GitHub repository: `iscc/iscc-codes`
- Documentation source branch for the current site: `main`
- Published GitHub Pages branch: `gh-pages`
- GitHub Pages source: `gh-pages` branch, repository root
- Custom domain file: `docs/CNAME` in the source branch and `CNAME` in the
  generated `gh-pages` branch

## Current public paths

The current sitemap lists these canonical paths:

- `/`
- `/capabilities/`
- `/concept/`
- `/license/`
- `/resources/`
- `/specification/`

These paths should remain valid throughout the migration. If a page is moved as
part of the new information architecture, keep the old path as a forwarding page
or configure an explicit redirect to the new location.

## Historical and compatibility paths

Historical paths are kept as redirects in `zensical.toml`
(`[project.plugins.redirects.redirect_maps]`). The generated redirect pages carry
a canonical link to the current page and stay out of the sitemap and search index.

- `/implementations/` → `/resources/`, carried over from the previous MkDocs
  configuration.
- `/features/` → `/capabilities/`, after the `Features` page was renamed to
  `Capabilities`.
- `/discovery/` → `/iscc-discovery-protocol-idp/`, after the Discovery Protocol
  page moved from its first published path to a descriptive one.

Keep these compatibility paths covered in future content architecture changes.
`/implementations/` may become a redirect to a future implementations, ecosystem,
or developer-resources page, but neither path should become a bare 404.

## Source path mapping

Current source files for the public paths:

- `/` → `docs/index.md`
- `/capabilities/` → `docs/capabilities.md`
- `/concept/` → `docs/concept.md`
- `/iscc-discovery-protocol-idp/` → `docs/iscc-discovery-protocol-idp.md`
- `/license/` → `docs/license.md`
- `/resources/` → `docs/resources.md`
- `/specification/` → `docs/specification.md`
- `/implementations/`, `/features/` and `/discovery/` → redirects in `zensical.toml`

## Migration rules

- Preserve the custom domain `iscc.codes`.
- Preserve all current public paths listed above.
- Preserve `/implementations/` as a compatibility path.
- Preserve `/features/` as a compatibility path forwarding to `/capabilities/`.
- Preserve `/discovery/` as a compatibility path forwarding to
  `/iscc-discovery-protocol-idp/`.
- Prefer neutral maintainer vocabulary such as "site migration", "URL
  preservation", "link compatibility", "redirect map", and "canonical paths".
- Avoid repository structure or public docs that frame this work as marketing.
- Keep early migration pull requests mechanical and reviewable: first preserve
  paths, then change the documentation engine, then update stale content.
- Keep the retired Python proof-of-concept out of the repository. The archival
  source was removed and now lives only in git history at [`legacy/python-poc/`
  as of commit `7610643`](https://github.com/iscc/iscc-codes/tree/7610643b9646b61ebe8882dd39a492742159e73c/legacy/python-poc);
  the PyPI wrapper scaffold lives in `pypi/iscc-wrapper/`.

## Verification

Run the source compatibility check from the repository root:

```bash
python scripts/check_site_paths.py
```

After generating a site, pass the output directory as well:

```bash
python scripts/check_site_paths.py --site-dir site
```

The check verifies that required source pages exist and, when a generated site
is provided, that the generated output still contains the required public paths.

## Zensical migration baseline

The documentation engine is now configured by `zensical.toml`. The legacy
`mkdocs.yml` file has been removed from the source branch to avoid two competing
site configurations.

The migration baseline carries over:

- Navigation for the six canonical paths.
- `docs/implementations.md` as a compatibility forwarding page for
  `/implementations/`.
- `docs/CNAME` for the custom domain.
- Plausible analytics through the existing custom analytics partial.
- Social footer links from the former MkDocs configuration.

Re-run `scripts/check_site_paths.py` against the generated output before
publishing.

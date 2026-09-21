# zensical_iscc

Zensical theme for ISCC documentation sites. It applies the ISCC identity
(Edition 01, September 2026) on top of Zensical's modern Material variant and
carries the widgets the ISCC sites share: the "Copy page" split button, the
iscc.ai chat widget and Plausible analytics.

The directory is laid out as a Zensical theme so it can be extracted into a
published package without restructuring. Until then, each site vendors a copy
and points `custom_dir` at it.

## Layout

| Path | Purpose |
| --- | --- |
| `mkdocs_theme.yml` | Theme defaults: fonts off (self-hosted), favicon, features, palette |
| `main.html` | Brand stylesheets, social metadata, redirects, widget configuration |
| `partials/logo.html` | Primary signature in both colourways, switched by scheme |
| `partials/integrations/analytics/plausible.html` | Plausible analytics provider |
| `assets/iscc/tokens/iscc.css` | Identity tokens, verbatim from the brand kit (`build/tokens/iscc.css`) |
| `assets/iscc/theme.css` | Maps tokens onto Zensical variables and styles components |
| `assets/iscc/fonts/` | Readex Pro and JetBrains Mono WOFF2 subsets with OFL notices |
| `assets/iscc/logos/` | Signature and symbol SVGs from the brand kit |
| `assets/iscc/favicon.svg`, `favicon.ico`, `apple-touch-icon.png` | Icons from the brand kit |
| `assets/iscc/social-share.png` | Default Open Graph image |
| `assets/iscc/circle-rhythm-*.svg` | Decorative pattern for landing or footer bands |
| `assets/iscc/copypage.js` | "Copy page", "View as Markdown", "Edit on GitHub" |
| `assets/iscc/copilot.js`, `copilot.css` | iscc.ai chat widget loader and shadow-DOM styles |

Brand assets are copied from `../iscc-brand`. Refresh them from there rather
than editing the copies.

## Using the theme in a site

```toml
[project]
extra_css = ["stylesheets/custom.css"]   # site-specific styles only

[project.extra.iscc]
tagline = "International Standard Content Code"   # home page title suffix
copy_page = true                                  # default true
chat = true                                       # default false
# og_image = "assets/iscc/social-share.png"       # default

[project.extra.analytics]
provider = "plausible"
domain = "iscc.codes"
# src = "https://stats.iscc.codes/js/plausible.js"  # default

[project.theme]
custom_dir = "zensical_iscc"
# features = [...]  # optional; overrides the theme's default feature list
```

The theme sets `font = false` and serves the brand fonts itself. Do not set
`theme.logo` or `theme.favicon` unless a site needs a different mark; the
theme provides both.

"Copy page" and "View as Markdown" read `index.md` next to each rendered page.
Generate those files after every build:

```bash
uv run zensical build --clean
uv run python scripts/gen_markdown_pages.py
```

The chat widget mounts only on origins that the iscc.ai token endpoint
allows, so it stays silent on localhost.

## Design decisions

- Light scheme: paper canvas, near-black text, white fields and code blocks
  with thin rules. Dark scheme: near-black canvas, navy code blocks, Sky Blue
  links.
- Blue is the link and primary action colour. Coral appears only in the logo,
  the current-page marker in navigation and text selection.
- Admonitions are labelled and coloured by role: note and info Sky Blue, tip
  and success Lime, warning Yellow, danger Coral. The dark scheme uses a left
  rule and coloured title instead of a filled field.
- Table headers, section labels and the footer directions use small JetBrains
  Mono capitals.
- `.iscc-unit--meta`, `--semantic`, `--content`, `--data`, `--instance` colour
  ISCC-UNIT labels consistently; always pair them with the unit name.
- Motion: 160 ms ease-out, disabled under `prefers-reduced-motion`.

## Extracting into a package

1. Move this directory into a new repository as `zensical_iscc/` and add an
   empty `__init__.py`.
2. Register the entry point in `pyproject.toml`:

   ```toml
   [project.entry-points."mkdocs.themes"]
   zensical_iscc = "zensical_iscc"
   ```

3. Ship `scripts/gen_markdown_pages.py` as a console script.
4. Sites then replace `custom_dir = "zensical_iscc"` with
   `name = "zensical_iscc"` and can still use `custom_dir` for their own
   overrides.

See <https://zensical.org/docs/customization/> for the packaging contract.

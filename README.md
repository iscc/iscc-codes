# ISCC Codes Documentation Site

[![DOI](https://zenodo.org/badge/96668860.svg)](https://zenodo.org/badge/latestdoi/96668860)

| WARNING: This repository is the source for the `iscc.codes` documentation site and preserves historical ISCC Version 1.1 material for continuity. The old Python proof-of-concept code has been retired from the repository root and is not the current ISCC implementation. |
| --- |

The **International Standard Content Code** is an [open standard](https://en.wikipedia.org/wiki/Open_standard) for content-derived digital media identification.

This repository now serves three purposes:

- source for the public documentation site at <https://iscc.codes/>
- historical ISCC Version 1.1 specification material, kept so existing URLs remain useful
- a pointer, via git history, to the early Python proof-of-concept that used the PyPI name [`iscc`](https://pypi.org/project/iscc/)

## Current Python package

New Python integrations should not use the old `iscc` proof-of-concept package.

- [`iscc-sdk`](https://github.com/iscc/iscc-sdk) - high-level toolkit for generating ISCCs from media files. Install with `pip install iscc-sdk`.
- [`iscc-core`](https://github.com/iscc/iscc-core) - lower-level implementation of the ISCC core algorithms used by the SDK. Install with `pip install iscc-core` when you need direct algorithm access.

For most application developers, start with `iscc-sdk`.

## Legacy `iscc` PyPI package

The PyPI package named [`iscc`](https://pypi.org/project/iscc/) was an early proof-of-concept that predates ISO 24138:2024 and the current `iscc-sdk` / `iscc-core` stack. It is retained only for compatibility with existing pinned installations and should not be used for new work.

The old source tree has been removed from the repository to clear its unmaintained dependency vulnerabilities. It remains archived in git history at [`legacy/python-poc/` as of commit `7610643`](https://github.com/iscc/iscc-codes/tree/7610643b9646b61ebe8882dd39a492742159e73c/legacy/python-poc). A small replacement wrapper package scaffold lives in [`pypi/iscc-wrapper/`](pypi/iscc-wrapper/) for a future `iscc` 2.0.0 PyPI release that depends on `iscc-sdk` and points users to the maintained package. Because the wrapper does not preserve the retired proof-of-concept API, users who need the old behavior should pin `iscc<2`.

Maintainers: see [`maintainers/pypi-iscc-retirement.md`](maintainers/pypi-iscc-retirement.md) before publishing anything under the `iscc` package name.

## Working with the documentation site

The documentation site is written in Markdown and built with [Zensical](https://zensical.org/). To build and serve it locally:

```bash
git clone https://github.com/iscc/iscc-codes.git
cd iscc-codes
python -m pip install zensical==0.0.43
zensical serve
```

Documentation source files live in [`docs/`](docs/). The site configuration lives in [`zensical.toml`](zensical.toml).

Run the compatibility checks before changing site paths:

```bash
python scripts/check_site_paths.py
zensical build --clean
python scripts/check_site_paths.py --site-dir site
```

## Contribute

Pull requests and other contributions are welcome. Use [GitHub Issues](https://github.com/iscc/iscc-codes/issues) to discuss ideas for the `iscc.codes` documentation site and ISCC resources. You may also join the developer chat on Telegram at <https://t.me/iscc_dev>.

## License

Documentation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The retired proof-of-concept code (archived in git history at [`legacy/python-poc/` as of commit `7610643`](https://github.com/iscc/iscc-codes/tree/7610643b9646b61ebe8882dd39a492742159e73c/legacy/python-poc)) and the wrapper package scaffold in `pypi/iscc-wrapper/` are licensed under BSD-2-Clause.

# Retiring the `iscc` PyPI Package

This note records the package-retirement policy for the historical PyPI project [`iscc`](https://pypi.org/project/iscc/).

## Status

- The `iscc` package name was used by an early Python proof-of-concept.
- That proof-of-concept predates ISO 24138:2024 and the current package split.
- Current Python integrations should use [`iscc-sdk`](https://pypi.org/project/iscc-sdk/) for application-level work.
- [`iscc-core`](https://pypi.org/project/iscc-core/) remains the lower-level core algorithm implementation used by the SDK.
- The retired proof-of-concept source is archived in `legacy/python-poc/`.
- A replacement wrapper package scaffold is available in `pypi/iscc-wrapper/`.

## Policy

Do not yank or delete historical `iscc` releases. Yanking breaks reproducible installs for users who pinned old versions and does not create a helpful migration path.

If the `iscc` package name is updated on PyPI, publish a final compatibility/wrapper release that:

1. depends on `iscc-sdk`, so `pip install iscc` pulls in the maintained high-level toolkit;
2. exposes a minimal `iscc` module that warns users to import `iscc_sdk` directly;
3. marks the project as inactive in PyPI classifiers;
4. uses the PyPI long description to point developers to `iscc-sdk`, `iscc-core`, and <https://iscc.codes/>;
5. avoids claiming API compatibility with the retired proof-of-concept.

## Suggested release shape

Use `pypi/iscc-wrapper/` as the source for the final release. It intentionally does not include the historical implementation.

Recommended version: `1.2.0` or another stable version greater than the current stable `1.0.5`, so a plain `pip install iscc` receives the migration package instead of the old proof-of-concept. Coordinate this with the package owners before publishing.

Recommended maintainer checklist:

```bash
cd pypi/iscc-wrapper
python -m build
python -m twine check dist/*
# Publish only after human review and PyPI owner approval:
# python -m twine upload dist/*
```

Publishing to PyPI is an external side effect and must not be done from routine documentation PRs.

## User-facing message

Use this wording consistently:

> The `iscc` PyPI package name was used by an early proof-of-concept. New Python integrations should install and import `iscc-sdk`. Use `iscc-core` only when you need lower-level algorithm access.

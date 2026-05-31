# Retiring the `iscc` PyPI Package

This note records the package-retirement policy for the historical PyPI project [`iscc`](https://pypi.org/project/iscc/).

## Status

- The `iscc` package name was used by an early Python proof-of-concept.
- That proof-of-concept predates ISO 24138:2024 and the current package split.
- Current Python integrations should use [`iscc-sdk`](https://pypi.org/project/iscc-sdk/) for application-level work.
- [`iscc-core`](https://pypi.org/project/iscc-core/) remains the lower-level core algorithm implementation used by the SDK.
- The retired proof-of-concept source was removed from the repository to clear its unmaintained dependency vulnerabilities; it remains archived in git history at [`legacy/python-poc/` as of commit `7610643`](https://github.com/iscc/iscc-codes/tree/7610643b9646b61ebe8882dd39a492742159e73c/legacy/python-poc).
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

Recommended version: `2.0.0`. The wrapper intentionally does not preserve the retired proof-of-concept API, so a major version is the honest signal and lets users pin `iscc<2` if they need the old behavior. Coordinate this with the package owners before publishing.

Recommended local maintainer checklist:

```bash
cd pypi/iscc-wrapper
uv build --out-dir dist --clear
uvx --from twine twine check dist/*
# Publish only after human review and PyPI owner approval:
# uv publish dist/*
```

Publishing to PyPI is an external side effect and must not be done from routine documentation PRs. The repository contains a guarded CI workflow in `.github/workflows/publish-iscc-wrapper.yml` that builds the wrapper on pull requests and publishes only from `iscc-v*` tags or an explicit manual dispatch with `publish=true`. It uses the organization-level `PYPI_TOKEN` secret as `UV_PUBLISH_TOKEN`.

For the first real publish, create and push a signed tag that matches the wrapper version exactly:

```bash
git tag -s iscc-v2.0.0 -m "iscc 2.0.0 wrapper release"
git push origin iscc-v2.0.0
```

## User-facing message

Use this wording consistently:

> The `iscc` PyPI package name was used by an early proof-of-concept. Starting with `iscc` 2.0.0 it is a breaking compatibility wrapper that installs `iscc-sdk` and points users to `iscc_sdk`. New Python integrations should install and import `iscc-sdk` directly. Use `iscc-core` only when you need lower-level algorithm access.

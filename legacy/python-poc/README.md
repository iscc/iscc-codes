# Legacy Python Proof of Concept

This directory archives the retired Python proof-of-concept that used the PyPI package name `iscc`.

It is kept for historical reference and for maintainers who need to inspect the old implementation. It is **not** the current ISCC implementation and should not be used for new integrations.

Use these packages instead:

- `iscc-sdk` — recommended high-level Python toolkit for application developers
- `iscc-core` — lower-level core algorithm implementation used by the SDK

The historical code predates ISO 24138:2024 and the current package architecture. It remains under BSD-2-Clause, but no feature development or routine maintenance is planned here.

If a final PyPI update for the `iscc` package is needed, prefer the wrapper package scaffold in `../../pypi/iscc-wrapper/` over republishing this old implementation.

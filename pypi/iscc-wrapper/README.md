# `iscc` PyPI Compatibility Wrapper

The `iscc` package name was used by an early ISCC proof-of-concept. That implementation is retired.

This wrapper is intended for a final PyPI release of `iscc` that installs the maintained [`iscc-sdk`](https://pypi.org/project/iscc-sdk/) package and warns developers to import `iscc_sdk` directly.

## New code

Use `iscc-sdk` directly:

```bash
pip install iscc-sdk
```

```python
import iscc_sdk as idk

meta = idk.code_iscc("/path/to/file")
print(meta.iscc)
```

Use `iscc-core` only when you need lower-level algorithm access.

## Compatibility behavior

This wrapper does not attempt to emulate the retired proof-of-concept API. It imports the public `iscc_sdk` top-level API as a convenience and emits a visible warning on import.

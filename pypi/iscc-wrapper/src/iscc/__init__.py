"""Deprecated compatibility wrapper for the historical `iscc` PyPI name.

New code should depend on and import `iscc_sdk` directly.
"""

from __future__ import annotations

from importlib import metadata
import warnings

warnings.warn(
    "The 'iscc' package 2.x is a breaking compatibility wrapper and no "
    "longer provides the original proof-of-concept API. Install and import "
    "'iscc_sdk' directly for new code: pip install iscc-sdk.",
    FutureWarning,
    stacklevel=2,
)

try:
    __version__ = metadata.version("iscc")
except metadata.PackageNotFoundError:  # pragma: no cover - local source tree
    __version__ = "0+local"

try:
    from iscc_sdk import *  # noqa: F401,F403
except ImportError as exc:  # pragma: no cover - dependency metadata should prevent this
    raise ImportError(
        "The deprecated 'iscc' compatibility wrapper requires 'iscc-sdk'. "
        "Install it with: pip install iscc-sdk"
    ) from exc

import warnings


def test_wrapper_import_warns_and_exposes_sdk_api():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        import iscc

    assert any("iscc_sdk" in str(item.message) for item in caught)
    assert hasattr(iscc, "code_iscc")

import os
import sys

import pytest


def test_tomli_availability():
    try:
        if sys.version_info >= (3, 11):  # sourcery skip: no-conditionals-in-tests
            import tomllib as tomli  # noqa: F401, I001
        else:
            import tomli  # noqa: F401
    except ImportError:
        pytest.fail("tomli package is not installed")


def test_toml_file_exists():
    assert os.path.exists("tdd.toml"), "tdd.toml file does not exist"


def test_toml_file_readable():
    assert os.access("tdd.toml", os.R_OK), "tdd.toml file is not readable"


def test_load_toml_file():
    if sys.version_info >= (3, 11):  # sourcery skip: no-conditionals-in-tests
        import tomllib as tomli  # noqa: F401, I001
    else:
        import tomli  # noqa: F401

    with open("tdd.toml", "rb") as f:
        try:
            config = tomli.load(f)
        except tomli.TOMLDecodeError as e:
            pytest.fail(f"Failed to parse TOML file: {str(e)}")

    assert isinstance(config, dict), "Loaded TOML should be a dictionary"


def test_default_section_exists():
    if sys.version_info >= (3, 11):  # sourcery skip: no-conditionals-in-tests
        import tomllib as tomli  # noqa: F401, I001
    else:
        import tomli  # noqa: F401

    with open("tdd.toml", "rb") as f:
        config = tomli.load(f)

    assert "DEFAULT" in config, "DEFAULT section not found in TOML file"


def test_default_section_values():
    if sys.version_info >= (3, 11):  # sourcery skip: no-conditionals-in-tests
        import tomllib as tomli  # noqa: F401, I001
    else:
        import tomli  # noqa: F401

    with open("tdd.toml", "rb") as f:
        config = tomli.load(f)

    default = config["DEFAULT"]
    assert default["ups_ae_title"] == "UPSSCP"
    assert default["qr_ae_title"] == "QRSCP"
    assert default["ae_title"] == "TDD"
    assert default["import_staging_directory"] == "~/tdd_import_staging"
    assert default["machine"] == "TR1"


def test_no_extra_sections():
    import tomli

    with open("tdd.toml", "rb") as f:
        config = tomli.load(f)

    assert len(config) == 1, "There should only be one section (DEFAULT) in the TOML file"


def test_comment_preservation():
    with open("tdd.toml", "r") as f:
        content = f.read()

    assert "# Our AE Title" in content, "Comment for AE Title should be preserved"
    assert "#   This directory contains the retrieved Composit IOD Instances" in content, (
        "Comment for import_staging_directory should be preserved"
    )


if __name__ == "__main__":
    pytest.main([__file__])

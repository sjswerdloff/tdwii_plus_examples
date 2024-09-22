import os

import pytest


def test_tomli_availability():
    try:
        import tomli  # noqa: F401
    except ImportError:
        pytest.fail("tomli package is not installed")


def test_toml_file_exists():
    assert os.path.exists("rtbdi.toml"), "rtbdi.toml file does not exist"


def test_toml_file_readable():
    assert os.access("rtbdi.toml", os.R_OK), "rtbdi.toml file is not readable"


def test_load_toml_file():
    import tomli

    with open("rtbdi.toml", "rb") as f:
        try:
            config = tomli.load(f)
        except tomli.TOMLDecodeError as e:
            pytest.fail(f"Failed to parse TOML file: {str(e)}")

    assert isinstance(config, dict), "Loaded TOML should be a dictionary"


def test_default_section_exists():
    import tomli

    with open("rtbdi.toml", "rb") as f:
        config = tomli.load(f)

    assert "DEFAULT" in config, "DEFAULT section not found in TOML file"


def test_default_section_values():
    import tomli

    with open("rtbdi.toml", "rb") as f:
        config = tomli.load(f)

    default = config["DEFAULT"]
    assert default["qr_ae_title"] == "OST"
    assert default["ae_title"] == "TMS"
    assert default["export_staging_directory"] == "~/BDIFolder"
    assert default["plan_path"] == "~/SamplePlanFolder"
    assert default["ups_scp_ae_title"] == "TMS"


def test_no_extra_sections():
    import tomli

    with open("rtbdi.toml", "rb") as f:
        config = tomli.load(f)

    assert len(config) == 1, "There should only be one section (DEFAULT) in the TOML file"


if __name__ == "__main__":
    pytest.main([__file__])

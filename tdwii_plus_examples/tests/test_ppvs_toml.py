import os

import pytest


def test_tomli_availability():
    try:
        import tomli  # noqa: F401
    except ImportError:
        pytest.fail("tomli package is not installed")


def test_toml_file_exists():
    assert os.path.exists("ppvs.toml"), "ppvs.toml file does not exist"


def test_toml_file_readable():
    assert os.access("ppvs.toml", os.R_OK), "ppvs.toml file is not readable"


def test_load_toml_file():
    import tomli

    with open("ppvs.toml", "rb") as f:
        try:
            config = tomli.load(f)
        except tomli.TOMLDecodeError as e:
            pytest.fail(f"Failed to parse TOML file: {str(e)}")

    assert isinstance(config, dict), "Loaded TOML should be a dictionary"


def test_default_section_exists():
    import tomli

    with open("ppvs.toml", "rb") as f:
        config = tomli.load(f)

    assert "DEFAULT" in config, "DEFAULT section not found in TOML file"


def test_default_section_values():
    import tomli

    with open("ppvs.toml", "rb") as f:
        config = tomli.load(f)

    default = config["DEFAULT"]
    assert default["ups_ae_title"] == "UPSSCP"
    assert default["qr_ae_title"] == "QRSCP"
    assert default["ae_title"] == "PPVS_SCP"
    assert default["import_staging_directory"] == "~/ppvs_import_staging"
    assert default["machine"] == "ProNova SC360 GR"


def test_no_extra_sections():
    import tomli

    with open("ppvs.toml", "rb") as f:
        config = tomli.load(f)

    assert len(config) == 1, "There should only be one section (DEFAULT) in the TOML file"


def test_no_listen_port():
    import tomli

    with open("ppvs.toml", "rb") as f:
        config = tomli.load(f)

    assert "listen_port" not in config["DEFAULT"], "listen_port should not be present (it's commented out)"


if __name__ == "__main__":
    pytest.main([__file__])

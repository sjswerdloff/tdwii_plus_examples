import json

import pytest

from tdwii_plus_examples.tdwii_config import (
    known_ae_ipaddr,
    known_ae_port,
    load_ae_config,
    load_machine_map,
    machine_ae_map,
)


@pytest.fixture
def sample_ae_config():
    return [
        {"AETitle": "OST", "IPAddr": "127.0.0.1", "Port": 11112},
        {"AETitle": "TDD", "IPAddr": "127.0.0.1", "Port": 11113},
        {"AETitle": "TMS", "IPAddr": "127.0.0.1", "Port": 11114},
    ]


@pytest.fixture
def sample_machine_map():
    return [{"machine": "FX1", "AETitle": "TDD"}, {"machine": "TR1", "AETitle": "TDD"}]


@pytest.fixture
def setup_config_files(tmp_path, sample_ae_config, sample_machine_map):
    ae_config_file = tmp_path / "ApplicationEntities.json"
    machine_map_file = tmp_path / "MachineMap.json"

    with open(ae_config_file, "w") as f:
        json.dump(sample_ae_config, f)

    with open(machine_map_file, "w") as f:
        json.dump(sample_machine_map, f)

    return ae_config_file, machine_map_file


def test_load_ae_config(setup_config_files):
    ae_config_file, _ = setup_config_files
    load_ae_config(str(ae_config_file))

    assert len(known_ae_ipaddr) == 3
    assert len(known_ae_port) == 3
    assert known_ae_ipaddr["OST"] == "127.0.0.1"
    assert known_ae_port["OST"] == 11112
    assert known_ae_ipaddr["TMS"] == "127.0.0.1"
    assert known_ae_port["TMS"] == 11114


def test_load_ae_config_default_path(setup_config_files, monkeypatch):
    ae_config_file, _ = setup_config_files
    monkeypatch.chdir(ae_config_file.parent)
    load_ae_config()

    assert len(known_ae_ipaddr) == 7
    assert len(known_ae_port) == 7


def test_load_machine_map(setup_config_files):
    _, machine_map_file = setup_config_files
    load_machine_map(str(machine_map_file))

    assert len(machine_ae_map) == 2
    assert machine_ae_map["FX1"] == "TDD"
    assert machine_ae_map["TR1"] == "TDD"


def test_load_machine_map_default_path(setup_config_files, monkeypatch):
    _, machine_map_file = setup_config_files
    monkeypatch.chdir(machine_map_file.parent)
    load_machine_map()

    assert len(machine_ae_map) == 3


def test_integration(setup_config_files):
    ae_config_file, machine_map_file = setup_config_files
    load_ae_config(str(ae_config_file))
    load_machine_map(str(machine_map_file))

    assert machine_ae_map["FX1"] == "TDD"
    assert known_ae_ipaddr[machine_ae_map["FX1"]] == "127.0.0.1"
    assert known_ae_port[machine_ae_map["FX1"]] == 11113


def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        load_ae_config("nonexistent_file.json")

    with pytest.raises(FileNotFoundError):
        load_machine_map("nonexistent_file.json")


if __name__ == "__main__":
    pytest.main([__file__])

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
        {"AETitle": "IMS_IHERO_TMS1", "IPAddr": "10.11.255.8", "Port": 10401},
        {"AETitle": "IHERO_SCP", "IPAddr": "10.11.255.8", "Port": 10403},
        {"AETitle": "TMS", "IPAddr": "127.0.0.1", "Port": 11114},
    ]


@pytest.fixture
def sample_machine_map():
    return [{"machine": "FX1", "AETitle": "IHERO_SCP"}, {"machine": "ProNova SC360 GR", "AETitle": "TDWII_SCP"}]


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
    assert known_ae_ipaddr["IMS_IHERO_TMS1"] == "10.11.255.8"
    assert known_ae_port["IMS_IHERO_TMS1"] == 10401
    assert known_ae_ipaddr["TMS"] == "127.0.0.1"
    assert known_ae_port["TMS"] == 11114


def test_load_ae_config_default_path(setup_config_files, monkeypatch):
    ae_config_file, _ = setup_config_files
    monkeypatch.chdir(ae_config_file.parent)
    load_ae_config()

    assert len(known_ae_ipaddr) == 3
    assert len(known_ae_port) == 3


def test_load_machine_map(setup_config_files):
    _, machine_map_file = setup_config_files
    load_machine_map(str(machine_map_file))

    assert len(machine_ae_map) == 2
    assert machine_ae_map["FX1"] == "IHERO_SCP"
    assert machine_ae_map["ProNova SC360 GR"] == "TDWII_SCP"


def test_load_machine_map_default_path(setup_config_files, monkeypatch):
    _, machine_map_file = setup_config_files
    monkeypatch.chdir(machine_map_file.parent)
    load_machine_map()

    assert len(machine_ae_map) == 2


def test_integration(setup_config_files):
    ae_config_file, machine_map_file = setup_config_files
    load_ae_config(str(ae_config_file))
    load_machine_map(str(machine_map_file))

    assert machine_ae_map["FX1"] == "IHERO_SCP"
    assert known_ae_ipaddr[machine_ae_map["FX1"]] == "10.11.255.8"
    assert known_ae_port[machine_ae_map["FX1"]] == 10403


def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        load_ae_config("nonexistent_file.json")

    with pytest.raises(FileNotFoundError):
        load_machine_map("nonexistent_file.json")


if __name__ == "__main__":
    pytest.main([__file__])

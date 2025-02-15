import json
import os

fdir = os.path.abspath(os.path.dirname(__file__))


known_ae_ipaddr = {}
known_ae_port = {}
machine_ae_map = {}


def load_ae_config(path_to_ae_config=None):
    if path_to_ae_config is not None:
        ae_config_file_path = path_to_ae_config
    else:
        ae_config_file = os.path.join(fdir, "./config/ApplicationEntities.json")
        ae_config_file_path = os.path.abspath(ae_config_file)
    with open(ae_config_file_path, "r") as f:
        ae_config_list = json.load(f)
    for ae in ae_config_list:
        known_ae_ipaddr[ae["AETitle"]] = ae["IPAddr"]
        known_ae_port[ae["AETitle"]] = ae["Port"]


def load_machine_map(path_to_machine_map=None):
    if path_to_machine_map is not None:
        machine_to_ae_config_file_path = path_to_machine_map
    else:
        machine_to_ae_config_file = os.path.join(fdir, "./config/MachineMap.json")
        machine_to_ae_config_file_path = os.path.abspath(machine_to_ae_config_file)
    with open(machine_to_ae_config_file_path, "r") as f:
        machine_to_ae_list = json.load(f)
    for machine in machine_to_ae_list:
        machine_ae_map[machine["machine"]] = machine["AETitle"]

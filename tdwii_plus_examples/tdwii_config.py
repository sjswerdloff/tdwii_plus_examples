import json
import sys

known_ae_ipaddr = {}
known_ae_port = {}
machine_ae_map = {}


def load_ae_config(path_to_ae_config=None):
    if path_to_ae_config is not None:
        ae_config_file = path_to_ae_config
    else:
        ae_config_file = "ApplicationEntities.json"
    with open(ae_config_file, "r") as f:
        ae_config_list = json.load(f)
    for ae in ae_config_list:
        known_ae_ipaddr[ae["AETitle"]] = ae["IPAddr"]
        known_ae_port[ae["AETitle"]] = ae["Port"]


def load_machine_map(path_to_machine_map=None):
    if path_to_machine_map is not None:
        machine_to_ae_config_file = path_to_machine_map
    else:
        machine_to_ae_config_file = "MachineMap.json"
    with open(machine_to_ae_config_file, "r") as f:
        machine_to_ae_list = json.load(f)
    for machine in machine_to_ae_list:
        machine_ae_map[machine["machine"]] = machine["AETitle"]


if __name__ == "__main__":
    ae_config_file = None
    machine_map_file = None
    if sys.argv is not None:
        if len(sys.argv) > 1:
            ae_config_file = sys.argv[1]
        if len(sys.argv) > 2:
            machine_map_file = sys.argv[2]

    load_ae_config(ae_config_file)
    print(known_ae_ipaddr)
    print(known_ae_port)
    load_machine_map(machine_map_file)
    print(machine_ae_map)
    for key in machine_ae_map:
        value = machine_ae_map[key]
        print(f"Machine Name:{key} AE Title:{value} IPAddr:{known_ae_ipaddr[value]} Port:{known_ae_port[value]}")

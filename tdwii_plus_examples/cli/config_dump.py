#!/usr/bin/env python
"""
This script loads and prints AE parameters and Machine Name mapping to AE Title.
Usage:
    config_dump.py <ae_config_file> <machine_map_file>
Arguments:
    ae_config_file: Path to the AE configuration file
        (default: tdwii_plus_examples/config/ApplicationEntities.json).
    machine_map_file: Path to the machine map file.
        (default: tdwii_plus_examples/config/MachineMap.json).
"""

import sys
from tdwii_plus_examples.tdwii_config import (
    load_ae_config, load_machine_map,
    known_ae_ipaddr, known_ae_port, machine_ae_map
)


def main():
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
        try:
            value = machine_ae_map[key]
            print(f"Machine Name:{key} AE Title:{value} "
                  f"IPAddr:{known_ae_ipaddr[value]} "
                  f"Port:{known_ae_port[value]}")
        except KeyError as e:
            print(f"AE Title {value} not found in AE config file")
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

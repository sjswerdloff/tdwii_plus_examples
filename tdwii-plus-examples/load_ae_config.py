import json

known_ae_ipaddr={}
known_ae_port={}
def load_ae_config():
    ae_config_file="ApplicationEntities.json"
    with open(ae_config_file,"r") as f:
        ae_config_list=json.load(f)
    for ae in ae_config_list:
        known_ae_ipaddr[ae["AETitle"]]= ae["IPAddr"]
        known_ae_port[ae["AETitle"]]=ae["Port"]

load_ae_config()
print(known_ae_ipaddr)
print(known_ae_port)
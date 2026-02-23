import json
import yaml

data_dict = {
    "rack": [
        {
            "server": {
                "dev_id": "S1",
                "server_name": "svr1",
                "domain": "biasc.be",
                "ip-address": "10.2.3.1",
                "os": "windows",
                "server_type": "vm",
                "services": [
                    {"service": "ad", "service_type": "vm", "protocol": "tcp", "port": "389"},
                    {"service": "dns", "service_type": "vm", "protocol": "udp", "port": "53"},
                    {"service": "ntp", "service_type": "vm", "protocol": "udp", "port": "123"}
                ]
            }
        }
    ]
}
yaml_str = "rack:\n- server:\n    dev_id: S1\n    server_name: svr1\n    domain: biasc.be\n    ip-address: 10.2.3.1\n    os: windows\n    server_type: vm\n    services:\n    - service: ad\n      service_type: vm\n      protocol: tcp\n      port: '389'\n    - service: dns\n      service_type: vm\n      protocol: udp\n      port: '53'\n    - service: ntp\n      service_type: vm\n      protocol: udp\n      port: '123'\n"
data_json_str = json.dumps(data_dict, indent=4)
data_yaml_str = yaml.dump(data_dict, sort_keys=False)
data_dict = yaml.load(yaml_str, Loader=yaml.FullLoader)
print(data_dict)


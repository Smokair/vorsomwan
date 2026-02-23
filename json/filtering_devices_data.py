import json

inventory_dict      = {}
inventory_list      = []
rack_struc          = {}
rack_struc["rack"]  = []
dev_dict            = {}
dev_list            = []
interfaces_dict      = {}
interfaces_list      = []

rack_struc = {
    "rack": [
        {
            "device": {
                "dev_id": "D1",
                "dev_name": "R1",
                "role": "router",
                "interfaces": [
                    {"interfaces": "GigabithEthernet1", "ipaddress": "10.0.1.1", "subnet mask": "255.255.255.0"},
                    {"interfaces": "GigabithEthernet2", "ipaddress": "10.0.3.1", "subnet mask": "255.255.255.0"},
                    {"interfaces": "GigabithEthernet3", "ipaddress": "10.0.4.1", "subnet mask": "255.255.255.0"}
                ]
            }
        },
        {
            "device": {
                "dev_id": "D2",
                "dev_name": "C1",
                "role": "core",
                "interfaces": [
                    {"interfaces": "VLAN1", "ipaddress": "10.0.1.2", "subnet mask": "255.255.255.0"},
                    {"interfaces": "VLAN2", "ipaddress": "10.0.2.1", "subnet mask": "255.255.255.0"},
                    {"interfaces": "VLAN20", "ipaddress": "10.0.20.1", "subnet mask": "255.255.255.0"}
                ]
            }
        },
        {
            "device": {
                "dev_id": "D3",
                "dev_name": "AC",
                "role": "access",
                "interfaces": [
                    {"interfaces": "VLAN2", "ipaddress": "10.0.2.2", "subnet mask": "255.255.255.0"}
                ]
            }
        }
    ]
}
js_groups = json.dumps(rack_struc)

print(type(rack_struc))
print(type(js_groups))
print(js_groups)
print(json.dumps(rack_struc, indent=4))

print("------2-------")
for g in rack_struc["rack"]:
    print("------2A------")
    print(type(g))
    print(g)
    print(g["device"]["interfaces"])
    for p in g ["device"]["interfaces"]:
        print(p)

print("------3-------")

for g in rack_struc["rack"]:
    for p in g["device"]["interfaces"]:
        print(p["ipaddress"])

import json

devices_struc = {
    "rack": [
        {
            "server": {
                "dev id": "S1",
                "server name": "svr1",
                "domain": "biasc.be",
                "ip-address": "10.2.3.1",
                "os": "Linux",
                "server type": "vm",
                "services": [
                    {"service": "ad", "service type": "vm", "protocol": "tcp", "port": "389"},
                    {"service": "dns", "service type": "vm", "protocol": "udp", "port": "53"},
                    {"service": "ntp", "service type": "vm", "protocol": "udp", "port": "123"}
                ]
            }
        },
        {
            "server": {
                "dev id": "S2",
                "server name": "svr2",
                "domain": "biasc.be",
                "ip-address": "10.2.3.2",
                "os": "Linux",
                "server type": "vm",
                "services": [
                    {"service": "flask", "service type": "vm", "protocol": "tcp", "port": "8089"},
                    {"service": "db", "service type": "vm", "protocol": "tcp", "port": "1521"}
                ]
            }
        },
        {
            "server": {
                "dev id": "S3",
                "server name": "svr3",
                "domain": "biasc.be",
                "ip-address": "10.2.3.3",
                "os": "Linux",
                "server type": "vm",
                "services": [
                    {"service": "dns", "service type": "vm", "protocol": "udp", "port": "53"},
                    {"service": "ntp", "service type": "vm", "protocol": "udp", "port": "123"},
                    {"service": "dhcp", "service type": "docker", "protocol": "udp", "port": "67"}
                ]
            }
        }
    ]
}

#print(devices_struc)

js_groups = json.dumps(devices_struc)

print(type(devices_struc))
print(type(js_groups))
print(js_groups)
print(json.dumps(devices_struc, indent=4))

print("-============2============")
for g in devices_struc["rack"]:
    print("-============2A============")
    print(type(g))
    print(g)
    print(g["server"]["services"])
    for p in g ["server"]["services"]:
        print(p)

print("============3============")
print(devices_struc.keys())

print("============3A============")
print(devices_struc["rack"][0].keys())
print(len(devices_struc["rack"]))

print("============3B============")
print(devices_struc["rack"][0]["server"].keys())
print(len(devices_struc["rack"][0]["server"]))

print("============3C============")
print(devices_struc["rack"][0]["server"]["services"][0].keys())
print(len(devices_struc["rack"][0]["server"]["services"]))


# Filter servers that use either TCP or UDP services
filtered_servers = []
rack_device_count = 0  # Variable to count devices per rack

for g in devices_struc["rack"]:
    server_info = g["server"]
    rack_device_count += 1  # Increment count for each device in the rack
    has_tcp_or_udp = False

    for service in server_info["services"]:
        if service["protocol"] in ["tcp", "udp"]:
            has_tcp_or_udp = True
            break
    
    if has_tcp_or_udp:
        filtered_servers.append(server_info)

# Output the filtered result and the count of devices per rack
print(f"Devices per rack: {rack_device_count}")
print(json.dumps(filtered_servers, indent=4))
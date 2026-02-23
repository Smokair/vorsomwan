import json

devices_struc = {
    "rack": [
        {
            "server": {
                "dev_id": "S1", "server_name": "svr1", "domain": "biasc.be", "ip-address": "10.2.3.1", "os": "linux" , "server-type": "vm", 
                "services":[
                    {"service": "ad", "service-type": "vm", "protocol": "tcp", "port": "389"},
                    {"service": "dns", "service-type": "vm", "protocol": "udp", "port": "53"},
                    {"service": "ntp", "service-type": "vm", "protocol": "udp", "port": "123"}
                ]
            }
        },
        {
            "server": {
                "dev_id": "S2", "server_name": "svr2", "domain": "biasc.be", "ip-address": "10.2.3.2", "os": "linux" , "server-type": "vm", 
                "services":[
                    {"service": "flask", "service-type": "vm", "protocol": "tcp", "port": "8089"},
                    {"service": "db", "service-type": "vm", "protocol": "tcp", "port": "1521"}
                ]
            }
        },        
        {
            "server": {
                "dev_id": "S3", "server_name": "svr3", "domain": "biasc.be", "ip-address": "10.2.3.3", "os": "linux" , "server-type": "vm", 
                "services":[
                    {"service": "dns", "service-type": "vm", "protocol": "tcp", "port": "8089"},
                    {"service": "ntp", "service-type": "vm", "protocol": "udp", "port": "123"},
                    {"service": "dhcp", "service-type": "vm", "protocol": "udp", "port": "67"}
                ]
            }
        }
        {
            "server": {
                "dev_id": "S4", "server_name": "svr4", "domain": "belnet.be", "ip-address": "10.2.3.4", "os": "linux" , "server-type": "vm", 
                "services":[
                    {"service": "dns", "service-type": "vm", "protocol": "tcp", "port": "8090"},
                    {"service": "ntp", "service-type": "vm", "protocol": "udp", "port": "123"}

                ]
            }
        }
    ]
}





# Filter servers that use either TCP or UDP services
filtered_servers = []
rack_device_count = 0  # Variable to count devices per rack

for g in devices_struc["rack"]:
    server_info = g["server"]
    rack_device_count += 1  # Increment count for each device in the rack
    has_tcp_or_udp = False

    for service in server_info["services"]:
        if service["protocol"] in ["tcp"]:
            has_tcp_or_udp = True
            break
    
    if has_tcp_or_udp:
        filtered_servers.append(server_info)

# Output the filtered result and the count of devices per rack
print(f"Devices per rack: {rack_device_count}")
print(json.dumps(filtered_servers, indent=4))

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
        },
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

# Filter for servers with TCP services
print("Server Name, IP Address, and TCP Ports:")
for g in devices_struc["rack"]:
    server_info = g["server"]
    tcp_ports = [service["port"] for service in server_info["services"] if service["protocol"] == "tcp"]

    if tcp_ports:  # If there are TCP ports, print them
        print(f"Server: {server_info['server_name']}, IP: {server_info['ip-address']}, TCP Ports: {', '.join(tcp_ports)}")

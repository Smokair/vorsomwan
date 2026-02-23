import ipaddress
import pandas as pd

def generate_subnets(base_network, num_hosts):
    subnets = []
    base_network = ipaddress.IPv4Network(base_network, strict=False)

    # Vind het kleinste prefix dat past bij het aantal hosts
    prefix = 32
    while (2 ** (32 - prefix)) - 2 < num_hosts:
        prefix -= 1

    # Verdeel het netwerk in subnetten
    for subnet in base_network.subnets(new_prefix=prefix):
        total_addresses = subnet.num_addresses
        usable_addresses = total_addresses - 2
        network_address = str(subnet.network_address)
        broadcast_address = str(subnet.broadcast_address)
        first_host = str(list(subnet.hosts())[0]) if usable_addresses > 0 else None
        last_host = str(list(subnet.hosts())[-1]) if usable_addresses > 0 else None
        
        subnets.append({
            "Subnet": str(subnet),
            "Subnetmasker": str(subnet.netmask),
            "Prefix": f"/{subnet.prefixlen}",
            "Totaal adressen": total_addresses,
            "Bruikbare adressen": usable_addresses,
            "Netwerkadres": network_address,
            "1ste hostadres": first_host,
            "Laatste hostadres": last_host,
            "Broadcastadres": broadcast_address,
        })
    
    return subnets

# Dynamische input
base_network = "192.168.0.0/16"  # Start vanaf 192.168.0.0
num_hosts = int(input("Voer het aantal benodigde hosts per subnet in: "))  # Dynamische input

# Genereer de subnetten
subnets = generate_subnets(base_network, num_hosts)

# Exporteer naar Excel
df = pd.DataFrame(subnets)
output_file = "/home/devasc/Documents/subnetten_192.168.0.x.xlsx"
df.to_excel(output_file, index=False)

print(f"Excel-bestand opgeslagen: {output_file}")

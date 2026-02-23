{
  "rack": [
    {
      "server": {
        "dev_id": "S1",
        "domain": "biasc.be",
        "ip-address": "10.2.3.1",
        "os": "windows",
        "server_name": "svr1",
        "server_type": "vm",
        "services": [
          {
            "port": "389",
            "protocol": "tcp",
            "service": "ad",
            "service_type": "vm"
          },
          {
            "port": "53",
            "protocol": "udp",
            "service": "dns",
            "service_type": "vm"
          },
          {
            "port": "123",
            "protocol": "udp",
            "service": "ntp",
            "service_type": "vm"
          }
        ]
      }
    },
    {
      "server": {
        "dev_id": "S2"
      }
    }
  ]
}

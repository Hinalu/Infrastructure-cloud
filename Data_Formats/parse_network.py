# Task Js3: Filter Network JSON Data
import json

# Simulated JSON response from DNA Center (GET /dna/intent/api/v1/network-device)
dnac_json_data = """
{
  "response": [
    {"hostname": "Router-01", "managementIpAddress": "192.168.56.101", "family": "Routers", "softwareVersion": "16.12.3"},
    {"hostname": "Switch-01", "managementIpAddress": "192.168.56.102", "family": "Switches & Hubs", "softwareVersion": "17.03.1"},
    {"hostname": "AP-Reception", "managementIpAddress": "192.168.56.105", "family": "Unified AP", "softwareVersion": "8.10.1"}
  ]
}
"""

def filter_network_devices():
    data = json.loads(dnac_json_data)
    
    print(f"{'Hostname':<20} {'IP Address':<15} {'Family':<15}")
    print("-" * 50)
    
    for device in data['response']:
        # Filter: Print specific fields for every device
        print(f"{device['hostname']:<20} {device['managementIpAddress']:<15} {device['family']:<15}")

if __name__ == "__main__":
    filter_network_devices()
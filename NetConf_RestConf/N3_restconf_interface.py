import requests
import json
from requests.auth import HTTPBasicAuth

# Task N3: RESTCONF Experiment (Python)
# Retrieves interface data using the REST API

HOST = '192.168.56.101'
PORT = '443'
USER = 'cisco'
PASS = 'cisco123!'

def get_restconf_interfaces():
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
    
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    
    print(f"GET Request to: {url}")
    
    # Verify=False to ignore self-signed cert warnings in lab
    response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)
    
    if response.status_code == 200:
        print("SUCCESS: Data Retrieved")
        data = response.json()
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    # Suppress SSL warnings
    requests.packages.urllib3.disable_warnings()
    get_restconf_interfaces()
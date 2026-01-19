import requests
import json
import urllib3
from requests.auth import HTTPBasicAuth

# Task Dna: Cisco DNA Center Sandbox Experiment
# Connects to the Always-On Sandbox to retrieve device inventory

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CONFIGURATION (Cisco DevNet Always-On Sandbox)
DNAC_URL = "https://sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PASS = "Cisco123!"

def get_auth_token():
    """
    Authenticates with DNAC and returns a session token.
    """
    url = f"{DNAC_URL}/dna/system/api/v1/auth/token"
    # Basic Auth is used ONLY to get the token
    response = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), verify=False)
    response.raise_for_status()
    return response.json()["Token"]

def get_device_list(token):
    """
    Retrieves list of network devices using the auth token.
    """
    url = f"{DNAC_URL}/dna/intent/api/v1/network-device"
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

if __name__ == "__main__":
    print("--- Authenticating with DNA Center ---")
    try:
        token = get_auth_token()
        print("[+] Token received.")
        
        print("--- Fetching Device Inventory ---")
        inventory = get_device_list(token)
        
        # Filtering Logic (Evaluation Requirement)
        print(f"\n{'Hostname':<25} {'Family':<20} {'Management IP':<15}")
        print("-" * 65)
        
        for device in inventory['response']:
            # Handle potential None values safely
            hostname = device.get('hostname') or "Unknown"
            family = device.get('family') or "Unknown"
            ip = device.get('managementIpAddress') or "Unknown"
            
            print(f"{hostname:<25} {family:<20} {ip:<15}")
            
    except Exception as e:
        print(f"[-] Error: {e}")
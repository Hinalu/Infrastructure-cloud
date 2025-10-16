### Shorter version of the two previous cells
## STEP 1 PREP
import requests
import datetime
import json

#Suppress credential warning for this exercise
requests.packages.urllib3.disable_warnings()
print ("Current date and time: ")
print (datetime.datetime.now())

#HARD CODED VARIABLES
DNAC_scheme = 'https://'
DNAC_authority = 'sandboxdnac2.cisco.com'

DNAC_port = ':443'
DNAC_path_token = '/dna/system/api/v1/auth/token'
DNAC_path = '/dna/intent/api/v1/network-device'
DNAC_user = input("Username? (devnetuser)")
DNAC_psw = input("Password? (Cisco123!)")

### STEP 2 TOKEN REQUEST
token_req_url = DNAC_scheme + DNAC_authority + DNAC_path_token
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth = auth, verify = False)

print ("API Return Code: " + str(req.status_code))
print ("Request URI: " + token_req_url)
print ("Username: " + DNAC_user)

resp = req.text
print (req.text)
token = req.json()['Token']
msg = req.json()['message']

print ("Recieved Token:")
print (token)
print ("Recieved msg:")
print (len(msg))

### STEP 3 
### REQUEST API SERVICE (USING X-AUTH-TOKEN) -- INVENTORY REQUEST

print ("Inventory Request - Network Devices")
# INVENTORY REQUEST
req_url = DNAC_scheme + DNAC_authority + DNAC_port + DNAC_path
print (req_url)
header_data = {'X-auth-token': token}
resp_devices = requests.request('GET', req_url, headers = header_data, verify = False)
print(resp_devices)
resp_devices_json = resp_devices.json()
print('------------------------------')

print(dir(resp_devices))
dev_dict = json.loads(resp_devices.text)
print (dev_dict["response"][0].keys())
print ('------------------------------')
print (type(resp_devices_json))
print ("Response (json):")
print (json.dumps(resp_devices_json, indent=2))

### keys
print(resp_devices_json.keys())

### STAP 4 (MANIER 1)
i = 0
ip_address = resp_devices_json["response"][i]["managementIpAddress"]
update_time = resp_devices_json["response"][i]["lastUpdated"] 
err_msg = resp_devices_json["response"][i]["errorDescription"] 
clct_stat = resp_devices_json["response"][i]["collectionStatus"] 

print (ip_address)
print (update_time)
print (err_msg)
print (clct_stat)

### STAP 4 (MANIER 2)
for cursor in resp_devices_json["response"]:
    ip_address = cursor["managementIpAddress"]
    print (ip_address)
    update_time = cursor["lastUpdated"]
    print (update_time)
    err_msg = cursor["errorDescription"]
    print (err_msg)
    clct_stat = cursor["collectionStatus"]
    print (clct_stat)
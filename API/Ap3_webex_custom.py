import requests
import json

# Task Ap3: Custom API Experiment (Webex)
# This script creates a room in Webex Teams using the API

# CONFIGURATION
ACCESS_TOKEN = "Bearer YOUR_ACCESS_TOKEN_HERE" # Replace with your token
URL = "https://webexapis.com/v1/rooms"

headers = {
    "Authorization": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "title": "DevNet Portfolio Project Room"
}

def create_room():
    response = requests.post(URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("SUCCESS: Room created successfully.")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"FAILED: Status Code {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    create_room()
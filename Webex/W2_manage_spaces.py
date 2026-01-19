import requests
import json
import time

# Task W2: Manage Webex Spaces (Create, Post, Delete)
# Also covers Skills Exam Task 6

# --- CONFIGURATION ---
ACCESS_TOKEN = "Bearer YOUR_ACCESS_TOKEN_HERE"  # REPLACE THIS!
BASE_URL = "https://webexapis.com/v1"
ROOM_NAME = "DevNet Skills Exam Room"
MESSAGE_TEXT = "Task 6: Webex Room Created via Python"

headers = {
    "Authorization": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def create_room():
    url = f"{BASE_URL}/rooms"
    payload = {"title": ROOM_NAME}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        room_id = response.json()['id']
        print(f"[+] Created Room: {ROOM_NAME} (ID: {room_id})")
        return room_id
    else:
        print(f"[-] Failed to create room: {response.text}")
        return None

def post_message(room_id):
    url = f"{BASE_URL}/messages"
    payload = {"roomId": room_id, "text": MESSAGE_TEXT}
    requests.post(url, headers=headers, json=payload)
    print(f"[+] Posted Message: '{MESSAGE_TEXT}'")

def delete_room(room_id):
    url = f"{BASE_URL}/rooms/{room_id}"
    requests.delete(url, headers=headers)
    print(f"[-] Deleted Room: {ROOM_NAME}")

if __name__ == "__main__":
    print("--- Starting Webex Lifecycle Experiment ---")
    
    # 1. Create
    rid = create_room()
    
    if rid:
        # 2. Post
        post_message(rid)
        
        # Wait so you can actually see it in the app
        print("Waiting 10 seconds before cleanup...")
        time.sleep(10)
        
        # 3. Delete (Clean up)
        delete_room(rid)
        
    print("--- Experiment Completed ---")
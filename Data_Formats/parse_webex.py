# Task Js2: Filter Webex JSON Data
import json

# Simulated JSON response from Webex API (GET /v1/rooms)
webex_json_data = """
{
  "items": [
    {"id": "Y2lzY28...", "title": "DevNet Study Group", "type": "group", "created": "2023-01-01T10:00:00"},
    {"id": "Y2lzY29...", "title": "Project Alpha", "type": "direct", "created": "2023-02-15T14:30:00"},
    {"id": "Y2lzY30...", "title": "Infrastructure Team", "type": "group", "created": "2023-03-10T09:00:00"}
  ]
}
"""

def filter_webex_rooms():
    data = json.loads(webex_json_data)
    print("--- Filtered Webex Rooms (Title & ID) ---")
    for room in data['items']:
        # Filter: Only print if it's a 'group' type room
        if room['type'] == 'group':
            print(f"Room: {room['title']} | ID: {room['id']}")

if __name__ == "__main__":
    filter_webex_rooms()
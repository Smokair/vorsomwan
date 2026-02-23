import requests
import json

# Access token for Webex API
access_token = "MmZkZjVlMGQtNzVkMi00ZTUzLThkN2QtYTAwZDJjOTQxYjY3ZDE1OTBkN2EtN2Fm_P0A1_71b6b34c-abff-4407-ac50-5e62323aed80"

# Base API URLs
url_rooms = 'https://api.ciscospark.com/v1/rooms'
url_memberships = 'https://api.ciscospark.com/v1/memberships'

# Headers for API requests
headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}

# Step 1: Retrieve all rooms created
print("Retrieving all rooms...")
response_rooms = requests.get(url_rooms, headers=headers)
rooms_data = response_rooms.json()

if "items" in rooms_data:
    for room in rooms_data["items"]:
        room_id = room["id"]
        room_title = room["title"]
        print(f"Deleting room: {room_title} (ID: {room_id})")
        
        # Step 2: Delete all memberships in the room
        response_memberships = requests.get(url_memberships, headers=headers, params={"roomId": room_id})
        memberships_data = response_memberships.json()

        if "items" in memberships_data:
            for membership in memberships_data["items"]:
                membership_id = membership["id"]
                print(f"  Removing membership ID: {membership_id}")
                requests.delete(f"{url_memberships}/{membership_id}", headers=headers)
        
        # Step 3: Delete the room
        delete_room_response = requests.delete(f"{url_rooms}/{room_id}", headers=headers)
        if delete_room_response.status_code == 204:
            print(f"  Successfully deleted room: {room_title}")
        else:
            print(f"  Failed to delete room: {room_title}, Error: {delete_room_response.status_code}")
else:
    print("No rooms found to delete.")

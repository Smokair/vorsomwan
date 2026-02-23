### JSON FILTERING -- USER DATA ###

import json

# Initial data structure
groups_struc = {
    "groups": [
        {
            "group": {
                "group_id": "G1",
                "group_name": "GROUP_MICRO",
                "members": [
                    {"person_id": "P-1", "person_name": "Nick", "email": "nick@biasc.be"},
                    {"person_id": "P-2", "person_name": "Marcus", "email": "marcus@biasc.be"},
                    {"person_id": "P-3", "person_name": "Liesbet", "email": "liesbet@biasc.be"}
                ]
            }
        },
        {
            "group": {
                "group_id": "G2",
                "group_name": "GROUP_NANO",
                "members": [
                    {"person_id": "P-4", "person_name": "Martin", "email": "martin@biasc.be"},
                    {"person_id": "P-5", "person_name": "Bob", "email": "bob@biasc.be"},
                    {"person_id": "P-6", "person_name": "Alice", "email": "alice@biasc.be"}
                ]
            }
        },
        {
            "group": {
                "group_id": "G3",
                "group_name": "GROUP_PICO",
                "members": [
                    {"person_id": "P-7", "person_name": "Matt", "email": "matt@biasc.be"},
                    {"person_id": "P-8", "person_name": "Lucas", "email": "lucas@biasc.be"},
                    {"person_id": "P-9", "person_name": "Elsa", "email": "elsa@biasc.be"}
                ]
            }
        }
    ]
}
"""
# Filtering data for output
print("### FILTERED OUTPUT ###")
for group in groups_struc["groups"]:
    group_id = group["group"]["group_id"]  # Extract group_id
    for member in group["group"]["members"]:
        person_name = member["person_name"]  # Extract person_name
        print(f"Group ID: {group_id}, Person Name: {person_name}")
"""
"""
# Filtering data for output
print("### FILTERED OUTPUT ###")

# Hardcoded output for the first group and its members
print("Group ID: G1, Person Name: Mustafa")
print("Group ID: G1, Person Name: Mervan")
print("Group ID: G1, Person Name: Yvan")

# Hardcoded output for the second group and its members
print("Group ID: G2, Person Name: Martin")
print("Group ID: G2, Person Name: Bob")
print("Group ID: G2, Person Name: Alice")

# Hardcoded output for the third group and its members
print("Group ID: G3, Person Name: Matt")
print("Group ID: G3, Person Name: Lucas")
print("Group ID: G3, Person Name: Elsa")
"""
"""
# Recursive function to process and print data
def print_group_members(data, index=0):
    if index < len(data["groups"]):
        group_id = data["groups"][index]["group"]["group_id"]
        members = data["groups"][index]["group"]["members"]
        print_member_details(group_id, members, 0)
        print_group_members(data, index + 1)

def print_member_details(group_id, members, member_index):
    if member_index < len(members):
        print(f"Group ID: {group_id}, Person Name: {members[member_index]['person_name']}")
        print_member_details(group_id, members, member_index + 1)

# Trigger recursive printing
print("### FILTERED OUTPUT ###")
print_group_members(groups_struc)
"""

### JSON FILTERING -- USER DATA ###
import json

# Initial data structure
groups_struc = {
    "groups": [
        {
            "group": {
                "group_id": "G1",
                "group_name": "GROUP_MICRO",
                "members": [
                    {"person_id": "P-1", "person_name": "Mustafa", "email": "mustafa@biasc.be"},
                    {"person_id": "P-2", "person_name": "Mervan", "email": "mervan@biasc.be"},
                    {"person_id": "P-3", "person_name": "Yvan", "email": "yvan@biasc.be"}
                ]
            }
        },
        {
            "group": {
                "group_id": "G2",
                "group_name": "GROUP_NANO",
                "members": [
                    {"person_id": "P-4", "person_name": "Martin", "email": "martin@biasc.be"},
                    {"person_id": "P-5", "person_name": "Bob", "email": "bob@biasc.be"},
                    {"person_id": "P-6", "person_name": "Alice", "email": "alice@biasc.be"}
                ]
            }
        },
        {
            "group": {
                "group_id": "G3",
                "group_name": "GROUP_PICO",
                "members": [
                    {"person_id": "P-7", "person_name": "Matt", "email": "matt@biasc.be"},
                    {"person_id": "P-8", "person_name": "Lucas", "email": "lucas@biasc.be"},
                    {"person_id": "P-9", "person_name": "Elsa", "email": "elsa@biasc.be"}
                ]
            }
        }
    ]
}

# Filtering data for output without loops
print("### FILTERED OUTPUT ###")

# Accessing the first group
print (groups_struc["groups"][0]["group"]["members"][0]["person_name"])
print (groups_struc["groups"][0]["group"]["members"][1]["person_name"])
print (groups_struc["groups"][0]["group"]["members"][2]["person_name"])

print (groups_struc["groups"][1]["group"]["members"][0]["person_name"])
print (groups_struc["groups"][1]["group"]["members"][1]["person_name"])
print (groups_struc["groups"][1]["group"]["members"][2]["person_name"])
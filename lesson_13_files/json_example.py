import json

users = [
    {'id': 'user1', 'name': 'name1', 'score': 100, 'is_qa': False, 'company': None},
    {'id': 'user2', 'name': 'name2', 'score': 200, 'is_qa': True, 'company': {'id': 'company1', 'name': 'name1'}}
]

# json_users = json.dumps(users, indent=4)

# with open('users.json', 'w') as f:
#     f.write(json_users)

with open('users.json', 'w') as f:
    json.dump(users, indent=4, fp=f)

with open('users.json', 'r') as f:
    users = json.load(f)
print(users[0])

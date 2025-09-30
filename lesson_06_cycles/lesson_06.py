# user = {
#     'id': 1,
#     'name': 'Ola',
#     'age': 23
# }

# if bool
# if user['age'] < 18:  # if true > continue
#     print("test test")
# elif user['age'] == 18:
#     print("adult")
# else:
#     print("wow")

# for cycle

users = [
    {
        'id': 1,
        'name': 'Ola',
        'age': 22},
    {
        'id': 2,
        'name': 'Max',
        'age': 20},
    {
        'id': 3,
        'name': 'Kat',
        'age': 23}

]
for user in users:
    print(user)
    pass

for user in users:
    if user['age'] != 20:
        continue
    if user['age'] == 23:
        print(user['name'])
        print("yes")
    else:
        print(user['name'])
        print("no")

users_list = [
    {
        'id': 1,
        'name': 'Ola',
        'age': 22,
        'tool': ['dev tools']},
    {
        'id': 2,
        'name': 'Max',
        'age': 20,
        'tool': ['dev tools', 'postman']},
    {
        'id': 3,
        'name': 'Kat',
        'age': 23,
        'tool': ['dev tools', 'pyharm']}

]

for user in users_list:
    user_data = list(user.values())
    print(user_data)
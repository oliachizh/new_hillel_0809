# lambda_name = lambda agr: arg > 5

def lambda_name(agr):
    return agr > 5
def get_ids(dct:dict):
    return dct['id']
users = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "age": 28, "country": "USA"},
    {"id": 7, "name": "Charlie Smith", "email": "bob@example.com", "age": 34, "country": "Canada"},
    {"id": 3, "name": "Bob Brown", "email": "charlie@example.com", "age": 22, "country": "UK"},
    {"id": 2, "name": "Diana Prince", "email": "diana@example.com", "age": 30, "country": "France"},
    {"id": 5, "name": "Ethan Clark", "email": "ethan@example.com", "age": 27, "country": "Australia"},
]

users_2 = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "age": 28, "country": "USA"},
    {"id": 7, "name": "Charlie Smith", "email": "bob@example.com", "age": 34, "country": "Canada"},
    {"id": 3, "name": "Bob Brown", "email": "charlie@example.com", "age": 22, "country": "UK"},
    {"id": 2, "name": "Diana Prince", "email": "diana@example.com", "age": 30, "country": "France"},
    {"id": 5, "name": "Ethan Clark", "email": "ethan@example.com", "age": 27, "country": "Australia"},
]

"""sorting """
users_list_1 = users.sort(key= lambda x: x['name'], reverse=False) #reverse=False 0>100 by default
users_2.sort(key= get_ids, reverse=False)
# print(users_2)

"""Enumerate"""

for index, user in enumerate(users_2):
    print(f"Index of {user}is {index}")


""" Filter """
filtered_users = filter(lambda x: len(x["country"]) <=3, users_2)
# print([user for user in filtered_users])

numbers = [1, 2, 3, 4, 5]
# → [1, 4, 9, 16, 25]
# num_squared = list(map(pow, numbers, [2 for i in range(len(numbers))]))
num_squared = list(map(lambda x: x**2, numbers))
# print(num_squared)

words = ["apple", "banana", "cherry", "date"]
words_uppercase = list(map(lambda x: x.upper(), words))
# print(words_uppercase)

num_strings = ["10", "20", "30", "40", "50"]
# num_int = list(map(lambda x: int(x), num_strings))
num_int = list(map(int, num_strings))

# print(type(num_int[0]))

words = ["python", "map", "function", "practice"]
# words_len = list(map(lambda x: len(x), words))
words_len = list(map(len, words))

# print(words_len)
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
# sum_list = list(map(lambda x, y: x+y, list1, list2))
sum_list = [x+y for x, y in zip(list1, list2)]
# print(sum_list)

"""any & all"""
numbers = [3, 5, 7, 10]
#Check if all numbers are positive
# Use all() to check if every number is > 0
print(all(x%2==0 for x in numbers))
print(all(x>0 for x in numbers))

words = ["apple", "banana", "", "cherry"]
# Use all() to check if all strings are non-empty
print(all(len(x)>0 for x in words))

numbers = [2, 4, 6, 8]
# Check if all numbers are even AND if any number > 5
# print(all(x%2 ==0 for x in numbers) and any(x>5 for x in numbers))

#Task 4: Check if all strings have length > 3 AND any string contains 'e'
words = ["ale", "bae", "che", "doe"]
# Use map(), all(), and any() together
# Expected output: False (because "bat" and "dog" are too short)

print(all(map(lambda x: len(x) == 3, words)) and
      any(map(lambda x: 'e' in x, words)))



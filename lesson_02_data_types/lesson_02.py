immutable_object = 24.2 #str, tuple, bool
print(hash(immutable_object))

#list, dict, set (mutable → not hashable)

""" tuple """
# Tuples cant be changed

names = ('alex', 'olga', 'llala')
print(names[0:2])


""" list """
# Lists can be changed(mutable) and takes more memory than tuples
names = ['alex', 'olga', 'llala']
# append()
names.append('alex') #adding one el to the end of the list
print(names)
""" extend () """
# extend() is a list method that adds elements from another iterable (list, tuple, string, set, etc.) to the end of the list.
# Unlike append(), which adds the whole object as a single element,
# extend() unpacks the iterable and adds each item separately.

"""insert()"""
#is a list method that allows you to insert an element at a specific position (index) in a list.
names.insert(0, 'karte')
print(names)

# index → position where the element will be inserted
# element → the value to insert
# It shifts existing elements to the right

""" pop() remove element by index (the last el by default) """
removed_name= names.pop(0)
print(names)
print(removed_name)

""" remove () by value """
names.remove('alex')
print(names)

""" Unpacking"""

first_name, *other_name = names
# print(first_name)
# print(other_name)

""" sort"""
numbers = [2, 1, 3]
new_sorted_list = sorted(numbers, reverse=True)
# print(new_sorted_list)
numbers.sort()
print(numbers)

""" list comprehension """
new_list = [k**2 for k in range(10)]
print(new_list)

""" dict """
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics", "CS"],
    "graduated": False
}
""" get key, value """
print(student)
print(student["name"])
print(student.get("name1", "default"))


""" dict comprehension """

copy_student = {k:len(k) for k in student}
# print(copy_student)

users = [
    {'id': 1, 'name':'Alice'},
    {'id': 2, 'name':'FGhjf'},
    {'id': 4, 'name':'FGhjf'},
    {'id': 3 , 'name':'FGhjf'},
]

ids = [user['id'] for user in users]
# print(ids)

""" popitem() removes the last inserted key-value pair. """

item = student.popitem()
print(item)
print(student)

""" zip()"""

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

zipped = zip(names, scores)
print(dict(zipped))

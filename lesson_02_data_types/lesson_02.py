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

""" sets """

# An unordered collection of unique elements.
# Defined with curly braces {} or with set().
# no duplicates, order doesn’t matter(cant be accesed by index))

set_comp = {k**2 for k in range(10)}
print(set_comp)

""" update"""
set_comp.update([1,2])
print(set_comp)

set_comp.add(3) # adding one el
print(set_comp)
# remove

set_comp.pop() # remove random element
print(set_comp)

set_comp.remove(81) # remove specified val
print(set_comp)

# logic operation
print(81 in set_comp)

# operations

registered_users = {'Den', 'Max'}
invited_users = {'Alice', 'Bob', 'Charlie', 'Den'}
print(registered_users & invited_users)
all_users = registered_users.union(invited_users)
print(all_users)
intersection_users = registered_users.intersection(invited_users)
print(intersection_users)

difference_users = registered_users.difference(invited_users)
print(difference_users)

diff_between_2_sets = registered_users.symmetric_difference(invited_users)
print(diff_between_2_sets)
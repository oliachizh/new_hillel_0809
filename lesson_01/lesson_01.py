# split('separator') > split the row and return a liost of the splited row
# row.split() > defolt split by spaces
row = "I love you Olga, you will find evrything you are looking for"
default_split = row.split()
print(default_split)
# print(row.split('love'))

""" STARTWITH AND ENDSWITH"""

# ''.startwith('yourword') ''.endswith('')

print(row.startswith('I love you Olga'))
print(row.endswith('for'))
print('I love' == row[:6])


""" IS UPPER / IS TITLE / IS LOWER"""

test = "I LOVE"
print(test.isupper())
print(test.istitle())
print(test.islower())

print(test.lower())
print(test.upper())
print(test.title())
print(test.capitalize())

""" .find('')"""

# string.find(substring, start=0, end=len(string))
# substring → the text you are looking for
#
# start → optional, where to start searching
#
# end → optional, where to stop searching
#
# Returns: the index of the first occurrence of the substring
#
# Returns -1 if the substring is not found



text = "Hello, world!"
print(text.find("world"))  # 7
print(text.find("Python")) # -1

""" .index('')"""
text = "Hello, Hello world!"
print(text.index('world')) #return index of the first occurrence


""" REPLACE"""

# string.replace(old, new, count=-1)
#
# old → substring you want to replace
# new → substring to replace with
# count → optional, number of replacements. Default -1 means replace all occurrences
#
# Returns: a new string with replacements (strings are immutable in Python).

new_text = text.replace("Hello", "World",1)
print(new_text)


""" .strip()"""

# str.strip() — remove whitespace (or characters)
# If chars is not provided, it removes leading and trailing whitespace (spaces, tabs, newlines).
#
# If chars is provided, it removes all characters in that set from both ends.
# Returns a new string — does not change the original string.
# Use lstrip() to remove only left, rstrip() to remove only right.


text = "Hellon"
clean_text = text.strip('n')
print(clean_text)


""" .split() """
text = "Hello, world!"
split_text = text.split()
print(split_text)
print('_'.join(split_text))

row = 'Banana, 1 , dd, 2'

for char in row:
    if char.isdigit():
        row = row.replace(char, str(int(char)))


print(row)
print(str('1'))


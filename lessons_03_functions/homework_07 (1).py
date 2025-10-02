# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from lesson_02_data_types.lesson_02 import scores


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_nums(num1, num2):
    return sum(num1, num2)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_num(lst):
    return sum(lst) / len(lst)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_text(text):
    return text[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def max_length_word(lst):
    max_len = filter(lambda x: x if len(x) == max(len(i) for i in lst) else None, lst)
    return list(max_len)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    res = str1.find(str2)
    if res:
        return res
    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


def compare_grades(grades1, grades2):
    result = {k: v - i for k, v in grades1.items() for y, i in grades2.items() if k == y}

    return result


grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78}
grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80}

result = compare_grades(grades_1, grades_2)


# print(result)

def solution(*args, sep="."):
    return sep.join(str(i) for i in args)


# print(solution(11,22,2003, sep='/'))

def create_profile(**kwargs):
    profile = {"name": "Unknown", "age": "Unknown", "city": "Unknown"}
    new = profile | kwargs
    return new


# print(create_profile(name="Bob", age='Unknown', job='Engineering'))
# → {'name': 'Bob', 'age': 'Unknown', 'city': 'Unknown'}

def order_summary(*items, **details):
    list_items = 'Items: ' + ", ".join(items)
    for k, v in details.items():
        list_items += f"\n{k}: {v}"
    return list_items


# print(order_summary("apple", "banana", "orange", total=12.5, paid=True))

def custom_greet(*names, **options):
    case = "Hello, "
    new = ""
    if options:
        if 'uppercase' not in options or options['uppercase'] == 'False':
            output = "".join([case + i + '!\n' for i in names])
        else:
            output = "".join([case + i.upper() + '!\n' for i in names])
        if 'greeting' in options:
            new = output.replace("Hello", options["greeting"])
        else:
            new = output

    return new


# print(custom_greet("Alice", "Bob", greeting="Hi", uppercase= True))

def greet_user(**info):
    name = info.get("name", "Anonymous")
    age = info.get("age", 0)
    return f"Hello, {name}! You are {age} years old."


# print(greet_user(name="Alice", age=25))
# print(greet_user())

def product_info(**kwargs):
    name = kwargs.get("name", "Unknown")
    price = kwargs.get("price", 0)
    discount = kwargs.get("discount", 0)
    return f"Output: Product: {name}, Price: {price}, Discount: {discount}%"


# print(product_info(name="Laptop", price=1200, discount=10))
# Output: Product: Laptop, Price: 1200, Discount: 10%

# print(product_info(price=500))
# Output: Product: Unknown, Price: 500, Discount: 0%

def calculate(*nums, **options):
    operation = options.get("operation", "sum")
    if nums:
        if operation == "avg":
            return sum(nums) / len(nums)
        elif operation == "max":
            return max(nums)
        else:
            return sum(nums)
    else:
        return f"Provide numbers"


# print(calculate(2, 4, 6, operation="sum"))  # → 12
# print(calculate(2, 4, 6, operation="avg"))  # → 4.0
# print(calculate(operation="max"))  # → 6
# print(calculate(2, 4, 6))                   # → 12 (default sum)

def student_report(*scores, **options):
    pass_mark = options.get("pass_mark", 50)
    honors_mark = options.get("honors_mark", 90)
    show_summary = options.get("show_summary", True)
    passing_nums = list(map(lambda x: x >= pass_mark, scores))
    if_all_pass = all(passing_nums)
    if_honor_present = any(map(lambda x: x >= honors_mark, scores))
    return f"Total students: {len(scores)}\nAll passed: {if_all_pass}\nHonors present: {if_honor_present}"


# print(student_report(50, 99, 99, honors_mark=100))

def employee_performance(*scores, **options):
    pass_mark = options.get("pass_mark", 60)
    honor_mark = options.get("honors_mark", 90)
    new_list = dict(scores)
    for k, v in new_list.items():
        if v < pass_mark:
            new_list.update({k: "Fail"})
        elif v >= pass_mark and v < honor_mark:
            new_list.update({k: "Pass"})
        else:
            new_list.update({k: "Honors"})
    return new_list


# print(employee_performance(("Alice", 95), ("Bob", 70), ("Charlie", 55)))
# → {'Alice': 'Honors', 'Bob': 'Pass', 'Charlie': 'Fail'}
def format_text(*words, **options):
    uppercase = options.get("uppercase", False)
    reverse = options.get("reverse", False)
    sep = options.get("sep", " ")
    if reverse:
        words = reversed(words)
    if uppercase:
        words = map(lambda x: x.upper(), words)
    return sep.join(words)


print(format_text("hello", "world"))
# → "hello world"

# print(format_text("hello", "world", uppercase=True))
# → "HELLO WORLD"

# print(format_text("one", "two", "three", reverse=True, sep="-"))
# → "three-two-one"

# print(format_text("good", "morning", "everyone", uppercase=True, reverse=True, sep=", "))
# → "EVERYONE, MORNING, GOOD"

from functools import reduce

numbers = [3, 8, 12, 5, 20]


def num_filter(nums):
    return list(map(lambda x: x * 2, filter(lambda x: x > 10, nums)))


# print(num_filter(numbers))

# You get a list of mixed strings (some messy).
# Use map() + lambda to:
# strip extra spaces,
# lowercase all words,
# and remove punctuation (., ,, !, ?)

data = ["  Apple!", "banana ", " Cherry?", "PEACH  ", "grape..."]


# → ['apple', 'banana', 'cherry', 'peach', 'grape']

def clean_data(data):
    return list(map(lambda x: x.strip('!.? ').lower(), data))


# print(clean_data(data))

def score_result(lst):
    pass_threshold = 60
    result = list(map(lambda x: f"{x}: Pass" if x >= pass_threshold else f"{x}: Fail", lst))
    return result


scores = [45, 67, 89, 32, 100, 76]
# ['Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']
# print(score_result(scores))

# [("python", 6), ("is", 2), ("awesome", 7)]
words = ["python", "is", "awesome"]


def check_length(lst):
    return list(map(lambda x: (x, len(x)), lst))


# print(check_length(words))

names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 17, 35, 14]


def check_ages(lst1, lst2):
    result = list(map(lambda x, y: f"{x}: {'Adult' if y >= 18 else 'Minor'}", lst1, lst2))
    return result


# print(check_ages(names, ages))
# ["Alice: Adult", "Bob: Minor", "Charlie: Adult", "Diana: Minor"]
# If age ≥ 18 → "Adult"
# If age < 18 → "Minor"

def apply_discount(lst):
    return list(map(lambda x: x * 0.9 if x > 100 else x, lst))


prices = [50, 150, 200, 80, 120]


# print(apply_discount(prices))


def student_assessment(*scores, **options):
    pass_mark = options.get("pass_mark", 50)
    honors_mark = options.get("honors_mark", 90)
    show_summary = options.get("show_summary", True)
    uppercase_names = options.get("uppercase_names", False)
    printed_ver = {}
    result = list(map(
        lambda x: f"{x[0].upper() if uppercase_names else x[0]}: {'Fail' if x[1] < pass_mark else 'Honor' if x[1] >= honors_mark else 'Pass'}",
        scores))
    if show_summary:
        printed_ver.update({'Total Students': len(scores), 'All passed': all(map(lambda x: x[1] >= pass_mark, scores)),
                            'Honors present': any(map(lambda x: x[1] >= honors_mark, scores)),})
        return ",\n".join(list(f"{k}: {v}" for k,v in printed_ver.items()))

    else:
        return result

# print(student_assessment(
#     ("Alice", 95), ("Bob", 67), ("Charlie", 45), ("Diana", 88),
#     pass_mark=50, honors_mark=90, uppercase_names=True, show_summary=False
# ))


def shopping_cart(*items, **options):
    discount_threshold = options.get("discount_threshold", 100)
    discount_percent = options.get("discount_percent", 10)
    uppercase_items = options.get("uppercase_items", False)
    show_summary = options.get("show_summary", True)
    total_item_cost = tuple(
        map(lambda x: (x[1] * x[2] - x[1] * x[2] * discount_percent / 100) if x[1] * x[2] > discount_threshold else x[1] * x[2],
            items))
    list_items_cost = list(map(
        lambda x, y: f"{x[0].upper() if uppercase_items else x[0]}: ${y}",
        items, total_item_cost))
    if show_summary:
        print("Summary:\n")
        exceeding_item = list(map(lambda x: x[0] if x[1] >= discount_threshold else '', zip((i[0] for i in items), total_item_cost)))
        summary = {'Total items': len(items), 'Total value': sum(total_item_cost),
                   'Items exceeding discount threshold': ",".join(i for i in exceeding_item if i)}
        for k,v in summary.items():
            print(f"{k}: {v}")

    return list_items_cost



# print(shopping_cart(
#     ("apple", 30, 3),
#     ("banana", 20, 2),
#     ("cherry", 50, 3),
#     discount_threshold=60,
#     discount_percent=10,
#
# ))
def make_dict(keys, values):
    return dict(zip(keys, values))
keys = ["a", "b", "c"]
values = [1, 2, 3]
# print(make_dict(keys, values))  # → {'a': 1, 'b': 2, 'c': 3}

def increment_values(dictionary, n):
    new_dict = {k:v+n for k, v in dictionary.items()}
    return new_dict

d = {"x": 5, "y": 10}
# print(increment_values(d, 3))  # → {'x': 8, 'y': 13}

def filter_dict(d, threshold):
    return dict(filter(lambda i: i[1] >=threshold, d.items()))

data = {"a": 5, "b": 10, "c": 2}
result_1 = filter_dict(data, 5)
# print(result_1)

def analyze_scores(students, pass_mark=60):
    filtered_scores = dict(map(lambda i: (i[0].upper(), i[1] * 10),
                               filter(lambda i: i[1] >= pass_mark, students.items())))

    return filtered_scores

students = {"Alice": 85, "Bob": 42, "Charlie": 70, "Diana": 95}
result = analyze_scores(students, pass_mark=60)
# print(result)

def apply_tax(products, tax_rate):
    """
    Docstring
    :param products:
    :param tax_rate:
    :return:
    """
    return dict(map(lambda x: (x[0].upper(), x[1]*tax_rate), products.items()))

products = {"apple": 1.5, "banana": 1.0, "mango": 2.5}
result = apply_tax(products, 1.2)
print(result)

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
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
    return sum(lst)/len(lst)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_text(text):
    return text[::-1]
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_length_word(lst):
    max_len =  filter(lambda x: x if len(x) == max(len(i) for i in lst) else None, lst)
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
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

def compare_grades(grades1, grades2):
    result = {k: v-i for k, v in grades1.items() for y, i in grades2.items() if k == y}

    return result

grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78}
grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80}

result = compare_grades(grades_1, grades_2)
# print(result)

def solution(*args, sep="."):
    return sep.join(str(i) for i in args)

print(solution(11,22,2003, sep='/'))
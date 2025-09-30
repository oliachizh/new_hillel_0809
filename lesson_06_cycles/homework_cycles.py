# input_to_check = set(input("Enter a str: "))
# print(input_to_check)
# if len(input_to_check) < 10:
#     print(False)
# else:
#     print(True)

# while True:
#     text_input = input("Enter a word: ")
#     if 'h' in text_input.lower():
#         break

# text_input = input("Enter a word: ")
# while 'h' not in text_input.lower():
#     text_input = input("Enter a word: ")

#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst_2 = [i for i in lst1 if isinstance(i, str)]
# print(lst_2)

def calculate_tax(user_income):
    # В змінній user_income ВЖЕ Є дохід користувача. Запитувати не треба.
    # Напиши свій код тут. Запиши результат в змінну tax_amount.
    if user_income < 10000:
        tax_amount = user_income * 0.1
    elif user_income <= 50000:
        tax_amount = user_income * 0.15
    else:
        tax_amount = user_income * 0.2
    return tax_amount

print(calculate_tax(9000))
print(9000*0.1)
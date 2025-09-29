from ufw.util import word_wrap


def greetings():
    name = 'Olga'
    return f"Hi {name}"

# print(greetings())

def cust_calculator(num1: int|float, num2: int|float, operation: str='+')-> int | float | None:
    if operation == '+':
        return num1+num2
    if operation == '-':
        return num1-num2
# result = cust_calculator(1,2)
# print(result)

def filter_diff(*original_list, key: str, values) ->list:
    result_dict = []
    for dct in original_list:
        if key in dct:
            if dct[key] == values:
                result_dict.append(dct)
        else:
            result_dict.append(dct)
    return result_dict

result = filter_diff({'name': 'ola', 'age': 35}, {'name': 'alex', 'age': 39}, key='names', values='ola')
# print(result)

def print_user_info(full_info=False, **kwargs):
    if full_info:
        for key, val in kwargs.items():
            return f"{key} = {val}"
    else:
        return f"name = {kwargs.get('name')}"

result_ = print_user_info(True, name='ola', age= 35)
# print(result_)

def filter_dicts(base_dict, *args, print_info=True, **kwargs):
    result_list = []
    full_list = [base_dict, args]
    if not kwargs:
        return full_list

    for dct in full_list:
        for k,v in kwargs.items():
            if k in dct:
                if dct[k] == v:
                    result_list.append(dct)
    return result_list



res = filter_dicts({'n': 'val', 'f':'wow'}, 'args', n='vals',f='wow')
# print(res)



def division(a,b):
    result = None
    try:
        result= a/b
    except (ZeroDivisionError, TypeError) as e:
        print("Sometghing went wrong: ", e)

    return result

# print(division(2,'w'))

def getting_data_from_db(user_id):
    user_id_in_db = None
    try:
        user_id_in_db = str(user_id*5+17)
        return {
            "user_id": user_id_in_db,
            "data": []
        }
    except Exception as e:
        raise e



# print(getting_data_from_db('18'))
class AgeError(Exception):
    def __init__(self, age):
        message = f"You are {age} years old."
        super().__init__(message)

class ProductError(Exception):
    def __init__(self, product):
        message = f"Product {product} does not have discounts."
        super().__init__(message)

def get_discount(age, product_id):
    discount_products = [1,2,5,6]
    if age < 18 or age > 60:
        raise AgeError(age)
    if product_id not in discount_products:
        raise ProductError(product_id)
    return 20

get_discount(18, 90)



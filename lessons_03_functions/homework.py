
def sum_numbers(*nums):
    return sum(nums)
# print(sum_numbers(1, 2, 3))        # 6
sum_numbers(10, 20, 30, 40) # 100


def flexible_greet(*args, **kwargs):
    for i in args:
        print(f"Hello {i}!")
    for key, val in kwargs.items():
        print(f"{key}: {val}")

# flexible_greet("Alice", "Bob", age=30, city="London")



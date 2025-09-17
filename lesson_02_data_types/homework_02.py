# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
  'Mercedes': ('silver', 2017, 2.4, 'sedan', 35000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2017, 2.4, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.4, 35000)

results = [k for k,y in car_data.items() if y[1] >= search_criteria[0] and y[2]>= search_criteria[1] and y[4] == search_criteria[2]]

# print(sorted(results[:5]))

# for k in car_data:
#     print(car_data[k][0])


# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 39, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 33, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 35, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 39, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

people_records.insert(0, ('', 'Ola', 36, 'Engineer', 'New York'))
people_records[1], people_records[5] = people_records[5], people_records[1]


# print(people_records)


check = all(people_records[i][2] >= 30 for i in [6, 10, 13])
print("All have age >= 30:", check)

person = ("Alice", "Smith", 30, "Engineer", "Boston")
print(person[2] >= 18)

employees = {
    "E001": ("Alice", "Manager", 75000),
    "E002": ("Bob", "Engineer", 60000),
    "E003": ("Charlie", "Designer", 50000),
    "E004": ("Diana", "Engineer", 65000)
}


# Print all employee names.
names = [v[0] for k,v in employees.items()]
print(names)
# Find the employee with the highest salary.
max_salary = max([val[-1] for val in employees.values()])

# Add a new employee "E005": ("Eva", "HR", 55000).
employees.update({
    "E005": ("Eva", "HR", 55000),
})

print(employees)
# Check if "E003" exists in the dictionary.
print("E003" in employees.keys())
# Remove "E002".


print(employees)

cars = {
    "Toyota": 25000,
    "BMW": 60000,
    "Audi": 55000,
    "Honda": 22000,
    "Ford": 30000
}
# Find all cars with price <= 30000.
filterd_car_list = [k for k, v in cars.items() if v <= 30000]
print(filterd_car_list)
# Sort cars by price.

# Print the cheapest and most expensive car.
cheapest_car = min(cars, key=cars.get)
most_expensive_car = max(cars, key=cars.get)

# print("Cheapest car:", cheapest_car, cars[cheapest_car])
# print("Most expensive car:", most_expensive_car, cars[most_expensive_car])

student = ("Alice", 21, "Biology", "Boston")
# 👉 Tasks:
#
# Print the student’s age.
#
# Check if the student is at least 18.
#
# Replace "Boston" with "New York" (hint: convert to list).

#

numbers = [10, 20, 30, 40, 50, 60]
# 👉 Tasks:
#
# Insert 15 at index 1.
#
# Swap the first and last element.
#
# Remove the number 40.
#
# Find the average of all numbers in the list.

# numbers.insert(1, 15)
# numbers.remove(40)
# print(numbers)
# average = sum(numbers) / len(numbers)
# print(average)

students = {
    "S001": ("Alice", 21, "Biology"),
    "S002": ("Bob", 19, "Math"),
    "S003": ("Charlie", 22, "History"),
    "S004": ("Diana", 20, "Physics"),
}

# Print all student names.
# Find the oldest student.
# Check if "S005" exists in the dictionary.
# Add a new student: "S005": ("Eva", 23, "Chemistry").
# Print the final dictionary.

# names = {val[0] for val in students.values()}
# print(names)
# oldest_student = max(val[1] for val in students.values())
# print(oldest_student)
# check = "S005" in students
# print(check)
# students.update({"S005": ("Eva", 23, "Chemistry")})
# print(students)

cars = {
    "Toyota": 25000,
    "BMW": 60000,
    "Audi": 55000,
    "Honda": 22000,
    "Ford": 30000
}

# Find all cars with price between 20000 and 40000.
# Sort the cars by price descending.
# Find the average car price.
# Check if there is a car priced exactly at 30000.

# cars_filtered = [car for car, v in cars.items() if v >= 20000 and v <= 40000]
# print(f"Cars: {cars_filtered}")
# avr_cars = sum(cars.values()) / len(cars)
# print(avr_cars)
# car_price_30000 = {k:v for k,v in cars.items() if v == 30000}
# print(car_price_30000)

employees = [
    ("Alice", "Manager", 75000),
    ("Bob", "Engineer", 60000),
    ("Charlie", "Designer", 50000),
    ("Diana", "Engineer", 65000),
    ("Eva", "HR", 55000)
]
# Tasks:
# Print the names of all Engineers.
#
# Find the highest-paid employee.
#
# Increase all salaries by 10% and print updated list.
#
# Convert this list into a dictionary with keys "E001", "E002", etc., where values are the employee tuples.
#


names = [employee[0] for employee in employees]
print(names)
max_salary = max([employee[-1] for employee in employees])
print(max_salary)

updated_list = [(employee[0], employee[1],employee[2]*0.1+employee[2]) for employee in employees]
keys = ["E00"+str(i) for i in range(1, len(updated_list)+1)]
print(updated_list)
print(keys)
new_dict = dict(zip(keys, updated_list))
print(new_dict)
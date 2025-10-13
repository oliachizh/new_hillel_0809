def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


# print(factorial(1))


def analyze_scores(students, pass_mark=60):
    if not isinstance(pass_mark, int):
        raise TypeError("Pass mark must be an integer.")
    if len(students) == 0:
        raise ValueError("Students list must not be empty.")
    filtered_scores = dict(map(lambda i: (i[0].upper(), i[1] * 10),
                                   filter(lambda i: i[1] >= pass_mark, students.items())))

    return filtered_scores
#
# students = {}
# result = analyze_scores(students)
# print(result)

def filter_dict(d, threshold):
    if not isinstance(threshold, int):
        raise TypeError("Threshold must be an integer.")
    return dict(filter(lambda i: i[1] >=threshold, d.items()))


def process_employees(employees, *, min_salary=3000, bonus_rate=0.1, uppercase_names=False, include_summary=False):
    # --- Validation ---
    if not isinstance(employees, dict):
        raise TypeError("employees must be a dictionary.")
    if not isinstance(bonus_rate, (int, float)) or not (0 <= bonus_rate <= 1):
        raise ValueError("bonus_rate must be a number between 0 and 1.")
    if not all(isinstance(sal, (int, float)) for sal in employees.values()):
        raise ValueError("All salaries must be numeric.")

    # --- Filter employees ---
    filtered = dict(filter(lambda item: item[1] >= min_salary, employees.items()))

    # --- Apply bonus ---
    updated = dict(map(lambda item: (item[0], round(item[1] * (1 + bonus_rate), 2)), filtered.items()))

    # --- Optional name formatting ---
    if uppercase_names:
        updated = {k.upper(): v for k, v in updated.items()}

    # --- Optional summary ---
    if include_summary:
        summary = {
            "count": len(updated),
            "average_salary": round(sum(updated.values()) / len(updated), 2) if updated else 0
        }
        return {"employees": updated, "summary": summary}

    return updated

employees = {"Alice": 2500, "Bob": 4000, "Charlie": 6000}

print(process_employees(employees, min_salary=3000, bonus_rate=0.2))
# → {'Bob': 4800.0, 'Charlie': 7200.0}

process_employees(employees, bonus_rate=0.1, uppercase_names=True, include_summary=True)
# → {
#     'employees': {'BOB': 4400.0, 'CHARLIE': 6600.0},
#     'summary': {'count': 2, 'average_salary': 5500.0}
#   }

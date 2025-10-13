lst1 = [None]

def sum_numbers(lst):
    list_of_sums = []
    for i in lst:
        try:
            list_of_sums.append(sum(int(num) for num in i.split(',')))
        except (TypeError, ValueError):
            raise ValueError(f"Invalid input: {i}")
        except Exception as e:
            raise Exception(f"Invalid input: {e}")
    return list_of_sums

# print(sum_numbers(lst1))

def calculate_sum_from_file(filename):
    sum_from_file = 0
    try:
        with open(filename, 'r') as file_:
            for line in file_:
                line = line.strip()
                if line:
                    try:
                        sum_from_file += int(line)
                    except (ValueError, TypeError):
                        print("cant do this")

    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    except (TypeError, ValueError):
        raise TypeError('cant do this')
    return sum_from_file

# print(calculate_sum_from_file('data.txt'))
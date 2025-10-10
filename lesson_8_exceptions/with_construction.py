# file_ = open('data.txt') # open the file for reading by providing the path to this file if not in the same directory
# data = file_.read() # reading data
# file_.close() # closing the file
# print(data)

# try:
#     file = None
#     file_ = open('data1.txt')
#     data = file_.read()
#     print(data)
# except FileNotFoundError:
#     print('File not found')
# finally:
#     if file is not None:
#         file_.close()

# try:
#     with open('data1.txt') as file_:
#         data = file_.read()
#         print(data)
# except FileNotFoundError:
#     raise FileNotFoundError('File not found')

def send_request(url, params):
    response = None
    # sending request
    response = {}
    if url == 'users/300':
        raise AssertionError(f"response is bad for {url} with {params}")
    return {'user_id': int(url.split(r'/')[-1])}
    if response is {}:
        print(f"response is bad for {url} with {params}")
        raise AssertionError(f"response is bad for {url} with {params}")

def test_users():
    for user_id in [1,2,3,300]:
        try:
            user_data = send_request(f"users/{user_id}", {})
        except AssertionError as e:
            print('something went wrong', user_id, e)
            continue

        assert user_data['user_id'] == user_id

# test_users()

# Помилка значення: Дільник повинен бути числом.
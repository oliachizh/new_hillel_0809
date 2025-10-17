import os


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
           return [line.strip() for line in file if line.strip()][-1]
    except FileNotFoundError:
        raise FileNotFoundError(f'File {file_name} not found')

def assert_true(username, password, message):
    assert f'Login event - Username: {username}, Status: {password}' in message, 'Login event - Username: {username}, Status: {password} is not correct'


def assert_file_exists(file_name):
    assert os.path.exists(file_name), "Log file was not created"



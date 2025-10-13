import unittest
from core.asserts.function_asserts import assert_user
def get_user_data(user_id):
    user_data = {
        1: {'id': 1, 'name': 'Olga', 'companies': ['company_1', 'company_2']},
        2: {'id': 2, 'name': 'Alex', 'companies': ['company_1', 'company_5']},
        3: {'id': 3, 'name': 'Bob', 'companies': ['company_1',]},
    }
    return user_data[user_id]

class TestGetUserData(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('Exectuted before all test in class')

    def setUp(self): #executed for each test
        print('setUp')


    def test_user_data(self):
        print('teardown')

    def test_get_user_data(self):
        user_data = get_user_data(1)
        user_name = 'Olga'
        companies_num = 2

        assert_user(actual_user=user_data,user_id=1, user_name=user_name, companies_num=companies_num)


if __name__ == '__main__':
    unittest.main()
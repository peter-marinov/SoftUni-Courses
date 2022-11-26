class Person:
    def __init__(self, first_name, last_name, age, id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__id = id

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


import unittest


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person("Luc", "Peterson", 25, '0352')

    def test_correct_id_expect_success(self):
        result = self.person._Person__id
        expected = '0352'
        self.assertEqual(result, expected)

    def test_age_expected_to_be_25(self):
        self.assertEqual(self.person.age, 25)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = "Luc Peterson"
        self.assertEqual(result, expected_result)

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = "Luc Peterson is 25 years old"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
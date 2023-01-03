from unittest import TestCase, main

#from exam_preparation.python_oop_retake_exam_23_august_2021.project.library import Library
from project.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library('Lib1')

    def test_correct_initializing(self):
        self.assertEqual('Lib1', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_with_empty_name(self):
        with self.assertRaises(ValueError) as ve:
            new_library = Library('')
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_when_not_existing(self):
        self.library.add_book('John', 'Book1')
        self.library.add_book('John', 'Book2')
        self.assertEqual({'John': ['Book1', 'Book2']}, self.library.books_by_authors)

    def test_add_book_when_existing(self):
        self.library.add_book('John', 'Book1')
        self.library.add_book('John', 'Book1')
        self.assertEqual({'John': ['Book1']}, self.library.books_by_authors)

    def test_add_reader_when_not_exists(self):
        self.library.add_reader('Smith')
        self.assertEqual({'Smith': []}, self.library.readers)

    def test_add_reader_when_exists(self):
        self.library.add_reader('Smith')
        expected_result = self.library.add_reader('Smith')
        self.assertEqual({'Smith': []}, self.library.readers)
        self.assertEqual("Smith is already registered in the Lib1 library.", expected_result)

    def test_rent_book_when_reader_not_exist(self):
        expected_result = self.library.rent_book('Smith', 'John', 'Book1')
        self.assertEqual("Smith is not registered in the Lib1 Library.", expected_result)

    def test_rent_book_when_author_not_exist(self):
        self.library.add_reader('Smith')
        expected_result = self.library.rent_book('Smith', 'John', 'Book1')
        self.assertEqual("Lib1 Library does not have any John's books.", expected_result)

    def test_rent_book_when_book_not_exist(self):
        self.library.add_reader('Smith')
        self.library.add_book('John', 'Book2')
        expected_result = self.library.rent_book('Smith', 'John', 'Book1')
        self.assertEqual("""Lib1 Library does not have John's "Book1".""", expected_result)

    def test_rent_book_when_all_conditions_are_satisfied(self):
        self.library.add_reader('Smith')
        self.library.add_book('John', 'Book1')
        self.library.add_book('John', 'Book2')
        expected_result = self.library.rent_book('Smith', 'John', 'Book1')
        self.assertEqual({'Smith': [{'John': 'Book1'}]}, self.library.readers)
        self.assertEqual({'John': ['Book2']}, self.library.books_by_authors)
        self.assertEqual(None, expected_result)


if __name__ == '__main__':
    main()
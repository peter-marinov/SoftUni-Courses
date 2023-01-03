import unittest

from project.bookstore import Bookstore


class TestBookStore(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore(15)
        self.books = {
            'Java for dummies': 10,
            'C++ Bible': 3
        }

    def test_correct_initializing(self):
        self.assertEqual(15, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_with_value_zero_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            bookstore = Bookstore(0)

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_correct_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        self.assertEqual(13, len(self.bookstore))

    def test_not_enough_space_to_receive_book_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Python Advanced', 3)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_add_new_book_correct(self):
        result = self.bookstore.receive_book('Python Advanced', 2)

        self.assertEqual("2 copies of Python Advanced are available in the bookstore.", result)
        self.assertEqual({"Python Advanced": 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_add_existing_book_correct(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        result = self.bookstore.receive_book('C++ Bible', 1)

        self.assertEqual("4 copies of C++ Bible are available in the bookstore.", result)

    def test_sell_book_that_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Python Advanced", 2)

        self.assertEqual("Book Python Advanced doesn't exist!", str(ex.exception))

    def test_sell_more_copies_than_available_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Java for dummies', 11)

        self.assertEqual("Java for dummies has not enough copies to sell. Left: 10", str(ex.exception))

    def test_successfully_selling_a_book(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        result = self.bookstore.sell_book('C++ Bible', 3)

        self.assertEqual("Sold 3 copies of C++ Bible", result)
        self.assertEqual(3, self.bookstore.total_sold_books)
        self.assertEqual({
            'Java for dummies': 10,
            'C++ Bible': 0
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_correct_str_method(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        expected_result = []
        expected_result.append('Total sold books: 0')
        expected_result.append('Current availability: 13')
        expected_result.append(' - Java for dummies: 10 copies')
        expected_result.append(' - C++ Bible: 3 copies')

        self.assertEqual('\n'.join(expected_result), str(self.bookstore))

if __name__ == '__main__':
    unittest.main()

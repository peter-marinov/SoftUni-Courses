from unittest import TestCase, main

#from unit_testinng_exam.project.toy_store import ToyStore
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_initializing(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_when_shelf_not_exists_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('a', 'milka')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_when_already_on_the_shelf_raise_exception(self):
        self.store.add_toy('B', 'milka')
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('B', 'milka')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual({
            "A": None,
            "B": 'milka',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_when_shelf_not_empty_raise_exception(self):
        self.store.add_toy('B', 'milka')
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('B', 'cat')
        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertEqual({
            "A": None,
            "B": 'milka',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_when_it_is_possible(self):
        self.store.add_toy('B', 'milka')
        expected_result = self.store.add_toy('G', 'cat')
        self.assertEqual("Toy:cat placed successfully!", expected_result)
        self.assertEqual({
            "A": None,
            "B": 'milka',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": 'cat',
        }, self.store.toy_shelf)

    def test_remove_toy_when_shelf_not_exist_raise_exception(self):
        self.store.add_toy('B', 'milka')
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('Z', 'milka')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({
            "A": None,
            "B": 'milka',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": 'cat',
        }, self.store.toy_shelf)

    def test_remove_toy_when_not_on_this_shelf_raise_exception(self):
        self.store.add_toy('B', 'milka')
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('C', 'milka')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual({
            "A": None,
            "B": 'milka',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_remove_toy_when_possible(self):
        self.store.add_toy('B', 'milka')
        self.store.add_toy('G', 'cat')
        expected_result = self.store.remove_toy('G', 'cat')
        self.assertEqual("Remove toy:cat successfully!", expected_result)
        self.assertEqual({
            "A": None,
            "B": 'milka',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)




if __name__ == '__main__':
    main()
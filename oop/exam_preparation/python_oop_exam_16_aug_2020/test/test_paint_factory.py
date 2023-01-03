from unittest import TestCase, main

#from exam_preparation.python_oop_exam_16_aug_2020.project.factory.paint_factory import PaintFactory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory('factory name', 3)

    def test_correct_initializing(self):
        self.assertEqual('factory name', self.factory.name)
        self.assertEqual(3, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_ingredient_not_valid_raise_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient('black', 2)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(te.exception))

    def test_add_ingredient_when_not_enough_space_raise_value_error(self):
        self.factory.add_ingredient('white', 1)
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient('yellow', 3)
        self.assertEqual({'white': 1}, self.factory.ingredients)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_up_to_3(self):
        self.factory.add_ingredient('white', 1)
        self.factory.add_ingredient('yellow', 1)
        self.factory.add_ingredient('white', 1)
        self.assertEqual(2, len(self.factory.ingredients))
        self.assertEqual({'white': 2, 'yellow': 1}, self.factory.ingredients)

    def test_remove_ingredient_when_not_exists_raise_key_error(self):
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient('white', 2)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_when_quantity_become_lower_than_zero_raise_value_error(self):
        self.factory.add_ingredient('white', 1)
        self.factory.add_ingredient('yellow', 1)
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient('white', 2)
        self.assertEqual({'white': 1, 'yellow': 1}, self.factory.products)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_when_possible(self):
        self.factory.add_ingredient('white', 1)
        self.factory.add_ingredient('yellow', 1)
        self.factory.remove_ingredient('white', 1)
        self.assertEqual({'white': 0, 'yellow': 1}, self.factory.ingredients)

    def test__repr__with_ingredients(self):
        self.factory.add_ingredient('white', 1)
        self.factory.add_ingredient('yellow', 1)
        self.assertEqual("Factory name: factory name with capacity 3.\n"
                         "white: 1\n"
                         "yellow: 1\n", repr(self.factory))

    def test__repr__when_no_ingredients(self):
        self.assertEqual("Factory name: factory name with capacity 3.\n", repr(self.factory))


if __name__ == '__main__':
    main()
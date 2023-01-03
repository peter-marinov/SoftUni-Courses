from unittest import TestCase, main

#from exam_preparation.python_oop_exam_15_august_2021.project.pet_shop import PetShop
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.shop = PetShop('Shop name')

    def test_correct_initializing(self):
        self.assertEqual('Shop name', self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_when_quantity_is_zero_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food('beer', 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))
        self.assertEqual({}, self.shop.food)

    def test_add_new_food(self):
        expected_result = self.shop.add_food('rice', 2.505)

        self.assertEqual({'rice': 2.505}, self.shop.food)
        self.assertEqual("Successfully added 2.50 grams of rice.", expected_result)

    def test_add_existing_food(self):
        self.shop.add_food('rice', 2.50)
        self.shop.add_food('cheese', 5.20)
        expected_result = self.shop.add_food('rice', 2.50)

        self.assertEqual({'rice': 5.00, 'cheese': 5.20}, self.shop.food)
        self.assertEqual("Successfully added 2.50 grams of rice.", expected_result)

    def test_add_pet_successfully(self):
        expected_result = self.shop.add_pet('Tom')

        self.assertEqual(['Tom'], self.shop.pets)
        self.assertEqual("Successfully added Tom.", expected_result)

    def test_add_pet_which_exists_expect_exception(self):
        self.shop.add_pet('Tom')
        self.shop.add_pet('Jerry')

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet('Tom')

        self.assertEqual(['Tom', 'Jerry'], self.shop.pets)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_which_not_exists_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('cheese', 'Jerry')

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_food_which_not_exists(self):
        self.shop.add_pet('Jerry')
        expected_result = self.shop.feed_pet('cheese', 'Jerry')

        self.assertEqual('You do not have cheese', expected_result)

    def test_feed_pet_when_not_enough_food(self):
        self.shop.add_pet('Jerry')
        self.shop.add_food('cheese', 5.20)

        expected_result = self.shop.feed_pet('cheese', 'Jerry')

        self.assertEqual({'cheese': 1005.20}, self.shop.food)
        self.assertEqual("Adding food...", expected_result)

    def test_feed_pen_when_there_is_enough_food(self):
        self.shop.add_pet('Jerry')
        self.shop.add_food('cheese', 500.20)

        expected_result = self.shop.feed_pet('cheese', 'Jerry')

        self.assertEqual({'cheese': 400.20}, self.shop.food)
        self.assertEqual("Jerry was successfully fed", expected_result)

    def test__repr__method_with_no_pets(self):
        actual_result = "Shop Shop name:\n" \
                        "Pets: "
        self.assertEqual(actual_result, repr(self.shop))

    def test__repr__method_with_pets(self):
        self.shop.add_pet('Tom')
        self.shop.add_pet('Jerry')
        
        actual_result = "Shop Shop name:\n" \
                        "Pets: Tom, Jerry"
        self.assertEqual(actual_result, repr(self.shop))

if __name__ == '__main__':
    main()
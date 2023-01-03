from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart('Lidl', 20.5)

    def test_correct_initializing(self):
        self.assertEqual('Lidl', self.shopping_cart.shop_name)
        self.assertEqual(20.5, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_wrong_shop_name_with_lower_letter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            shop_with_lower_letter = ShoppingCart('kaufland', 20.5)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_wrong_shop_name_with_number_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            shop_with_lower_letter = ShoppingCart('1aufland', 20.5)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_return_name(self):
        self.assertEqual('Lidl', self.shopping_cart.shop_name)

    def test_add_to_cart_product_with_price_100_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('salam', 100)

        self.assertEqual(f"Product salam cost too much!", str(ve.exception))

    def test_add_to_cart_product_with_price_less_than_100(self):
        expected_result = self.shopping_cart.add_to_cart('salam', 5)

        self.assertEqual({'salam': 5}, self.shopping_cart.products)
        self.assertEqual("salam product was successfully added to the cart!", expected_result)

    def test_remove_from_cart_when_no_product_in_it(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('salam')

        self.assertEqual(f"No product with name salam in the cart!", str(ve.exception))

    def test_remove_from_cart_when_product_exists(self):
        self.shopping_cart.add_to_cart('salam', 90)
        self.shopping_cart.add_to_cart('pizza', 20)
        result = self.shopping_cart.remove_from_cart('salam')

        self.assertNotIn('salam', self.shopping_cart.products)
        self.assertEqual({'pizza': 20}, self.shopping_cart.products)
        self.assertEqual("Product salam was successfully removed from the cart!", result)

    def test_add_two_shopping_carts(self):
        other_shop_cart = ShoppingCart('Kaufland', 25.5)
        self.shopping_cart.add_to_cart('a', 1.5)
        other_shop_cart.add_to_cart('b', 2.5)
        new_shopping_cart = self.shopping_cart + other_shop_cart

        self.assertEqual('LidlKaufland', new_shopping_cart.shop_name)
        self.assertEqual(46, new_shopping_cart.budget)
        self.assertEqual({'a': 1.5, 'b': 2.5}, new_shopping_cart.products)

    def test_buy_products_when_have_enough_budget(self):
        self.shopping_cart.add_to_cart('salam', 10.5)
        result = self.shopping_cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 10.50lv.', result)

    def test_buy_products_when_no_enough_budget_expect_value_error(self):
        self.shopping_cart.add_to_cart('salam', 90)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 69.50lv!", str(ve.exception))




if __name__ == '__main__':
    main()
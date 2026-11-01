import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.cart import MAX_NUMBERS_ORDERED
from aims.search import search_by_title

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD {MAX_NUMBERS_ORDERED}")))

    def make_cart_worth_100(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100))
        return cart

    def test_discount_20_percent(self):
        cart = self.make_cart_worth_100()
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80)

    def test_percent_over_100_raises(self):
        cart = self.make_cart_worth_100()
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

class TestSearchByTitle(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("The Lion King"))

    def test_exact_case(self):
        self.assertEqual(search_by_title(self.cart, "The Lion King").title, "The Lion King")

    def test_ignores_case(self):
        self.assertEqual(search_by_title(self.cart, "the lion king").title, "The Lion King")
        self.assertEqual(search_by_title(self.cart, "THE LION KING").title, "The Lion King")

    def test_not_found_returns_none(self):
        self.assertIsNone(search_by_title(self.cart, "Aladdin"))


if __name__ == "__main__":
    unittest.main()
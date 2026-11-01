import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.cart import MAX_NUMBERS_ORDERED

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

class TestSort(unittest.TestCase):
    def make_cart(self):
        cart = Cart()
        for title, cost in [("Lion King", 19.95), ("aladdin", 18.99), ("Bambi", 24.95)]:
            cart.add_dvd(DigitalVideoDisc(title, cost=cost))
        return cart

    def test_sort_by_title(self):
        titles = [d.title for d in self.make_cart().sort_by_title()]
        self.assertEqual(titles, ["aladdin", "Bambi", "Lion King"])

    def test_sort_by_cost(self):
        costs = [d.cost for d in self.make_cart().sort_by_cost()]
        self.assertEqual(costs, [18.99, 19.95, 24.95])


if __name__ == "__main__":
    unittest.main()
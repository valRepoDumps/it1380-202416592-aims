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


if __name__ == "__main__":
    unittest.main()
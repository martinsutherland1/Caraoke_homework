import unittest

from src.guest import Guest
from src.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ted Mosby", 25.00)

    def test_guest_has_name(self):
        self.assertEqual("Ted Mosby", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(25.00, self.guest.wallet)

    def test_guest_can_buy_something(self):
        fee = Room("Disco Room", 15.00)
        self.guest.pay_entry_fee(fee)
        self.assertEqual(10.00, self.guest.wallet)

import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song
from src.menu import Menu


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ted Mosby", 25.00, "Saturday night", "Disco Room")

    def test_guest_has_name(self):
        self.assertEqual("Ted Mosby", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(25.00, self.guest.wallet)

    def test_guest_can_pay_entry(self):
        fee = Room("Disco Room", 15.00)
        self.guest.pay_entry_fee(fee)
        self.assertEqual(10.00, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Saturday night", self.guest.song)

    def test_guest_can_buy_from_bar(self):
        order = Menu("Beer", 3.00)
        self.guest.buy_from_menu(order)
        self.assertEqual(22.00, self.guest.wallet)

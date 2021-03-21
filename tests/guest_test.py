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

    def test_let_guest_know_they_are_skint(self):
        guest_1 = Guest("Marshall Eriksson", 30.00,
                        "Night fever", "Disco Room")
        fee = Room("Disco Room", 15.00)
        self.guest.pay_entry_fee(fee)
        order_1 = Menu("Beer", 3.00)
        order_2 = Menu("Beer", 3.00)
        order_3 = Menu("Beer", 3.00)
        order_4 = Menu("Cocktail", 6.00)
        guest_1.pay_entry_fee(fee)
        guest_1.buy_from_menu(order_1)
        guest_1.buy_from_menu(order_2)
        guest_1.buy_from_menu(order_3)
        guest_1.buy_from_menu(order_4)
        self.assertEqual("Skint!", self.guest.is_guest_skint(guest_1))

    def test_let_guest_know_they_still_have_cash(self):
        guest_1 = Guest("Robin Scherbatsky", 50.00,
                        "Heart of glass", "Disco Room")
        fee = Room("Disco Room", 15.00)
        order_1 = Menu("Beer", 3.00)
        order_2 = Menu("Beer", 3.00)
        order_3 = Menu("Scotch", 5.00)
        order_4 = Menu("Cocktail", 6.00)
        guest_1.pay_entry_fee(fee)
        guest_1.buy_from_menu(order_1)
        guest_1.buy_from_menu(order_2)
        guest_1.buy_from_menu(order_3)
        guest_1.buy_from_menu(order_4)
        self.assertEqual("Still loaded!", self.guest.is_guest_skint(guest_1))

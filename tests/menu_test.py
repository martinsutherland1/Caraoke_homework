import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song
from src.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu("Beer", 3.50)

    def test_menu_has_item(self):
        self.assertEqual("Beer", self.menu.item)

    def test_item_has_price(self):
        self.assertEqual(3.50, self.menu.price)

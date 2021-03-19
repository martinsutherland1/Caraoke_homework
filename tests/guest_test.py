import unittest

from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Martin")

    def test_guest_has_name(self):
        self.assertEqual("Martin", self.guest.name)

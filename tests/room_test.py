import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.menu import Menu


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Disco room", 15.00)

    def test_room_has_name(self):
        self.assertEqual("Disco room", self.room.name)

    def test_can_add_guest_to_room(self):
        guest = Guest("Ted Mosby", 35.00, "Saturday night", "Disco Room")
        self.room.check_in_guest(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_can_remove_guest_from_room(self):
        guest = Guest("Ted Mosby", 35.00, "Saturday night", "Disco Room")
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_can_add_song_to_room(self):
        song = Song("Superman")
        self.room.song_list(song)
        self.assertEqual(11, self.room.song_count())

    def test_is_the_room_full(self):
        guest_1 = Guest("Ted Mosby", 35.00, "Saturday night", "Disco Room")
        guest_2 = Guest("Barney Stinson", 45.00,
                        "Eye of the tiger", "Disco Room")
        guest_3 = Guest("Lily Aldrin", 25.00, "1999", "Disco Room")
        guest_4 = Guest("Robin Scherbatsky", 50.00,
                        "Heart of glass", "Disco Room")
        guest_5 = Guest("Marshall Eriksson", 30.00,
                        "Night fever", "Disco Room")
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)
        self.room.check_in_guest(guest_3)
        self.room.check_in_guest(guest_4)
        self.room.check_in_guest(guest_5)
        self.assertEqual(True, self.room.is_room_full())

    def test_room_has_space(self):

        guest_1 = Guest("Ted Mosby", 35.00, "Saturday night", "Disco Room")
        guest_2 = Guest("Barney Stinson", 45.00,
                        "Eye of the tiger", "Disco Room")
        guest_3 = Guest("Lily Aldrin", 25.00, "1999", "Disco Room")
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)
        self.room.check_in_guest(guest_3)
        self.assertEqual(False, self.room.is_room_full())

    def test_room_has_playlist(self):
        self.assertEqual(10, self.room.songs_on_playlist())

    def test_is_guest_song_on_playlist(self):
        self.assertEqual("Whoo!", self.room.check_playlist("Saturday night"))

    def test_guest_song_not_on_playlist(self):
        self.assertEqual("Boo!", self.room.check_playlist("Night fever"))

    def test_guest_can_add_to_tab(self):
        guest_1 = Guest("Ted Mosby", 35.00, "Saturday night", "Disco Room")
        fee = Room("Disco Room", 15.00)
        order = Menu("Beer", 3.50)
        guest_1.pay_entry_fee(fee)
        guest_1.buy_from_menu(order)
        self.assertEqual(18.50, guest_1.tab)

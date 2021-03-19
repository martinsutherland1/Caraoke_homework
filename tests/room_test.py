import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Disco room")

    def test_room_has_name(self):
        self.assertEqual("Disco room", self.room.name)

    def test_can_add_guest_to_room(self):
        guest = Guest("Ted Mosby")
        self.room.check_in_guest(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_can_remove_guest_from_room(self):
        guest = Guest("Ted Mosby")
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_can_add_song_to_room(self):
        song = Song("Saturday night")
        self.room.song_list(song)
        self.assertEqual(1, self.room.song_count())

    def test_is_the_room_full(self):
        guest_1 = Guest("Ted Mosby")
        guest_2 = Guest("Barney Stinson")
        guest_3 = Guest("Lily Aldrin")
        guest_4 = Guest("Robin Scherbatsky")
        guest_5 = Guest("Marshall Eriksson")
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)
        self.room.check_in_guest(guest_3)
        self.room.check_in_guest(guest_4)
        self.room.check_in_guest(guest_5)
        self.assertEqual(True, self.room.is_room_full())

    def test_room_has_space(self):

        guest_1 = Guest("Ted Mosby")
        guest_2 = Guest("Barney Stinson")
        guest_3 = Guest("Lily Aldrin")
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)
        self.room.check_in_guest(guest_3)
        self.assertEqual(False, self.room.is_room_full())

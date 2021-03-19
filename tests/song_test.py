import unittest

from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Best")

    def test_song_has_title(self):
        self.assertEqual("The Best", self.song.title)

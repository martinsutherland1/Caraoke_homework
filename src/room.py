

class Room:
    def __init__(self, name, fee):
        self.name = name
        self.guests = []
        self.songs = ["The Best", "Eye of the tiger", "1999", "Heart of glass", "Saturday night",
                      "Stayin' alive", "Disco inferno", "We are family", "I will survive", "Super freak"]
        self.fee = fee
        self.menu = {"Beer": 3.00, "Burger": 4.50, "Wine": 4.00, "Chips": 2.50}

    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest_to_room):
        self.guests.append(guest_to_room)

    def check_out_guest(self, guest_to_remove):
        self.guests.remove(guest_to_remove)

    def song_list(self, new_song):
        self.songs.append(new_song)

    def song_count(self):
        return len(self.songs)

    def is_room_full(self):
        if self.guest_count() == 5:
            return True
        else:
            return False

    def playlist(self, song):
        self.songs.append(song)

    def songs_on_playlist(self):
        return len(self.songs)

    def check_playlist(self, fave_song):
        for song in self.songs:
            if fave_song == song:
                return "Whoo!"
        return "Boo!"

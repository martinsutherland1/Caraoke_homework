class Room:
    def __init__(self, name, fee):
        self.name = name
        self.guests = []
        self.songs = []
        self.fee = fee

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

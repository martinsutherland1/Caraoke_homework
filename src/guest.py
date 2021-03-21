class Guest:
    def __init__(self, name, wallet, song, room):
        self.name = name
        self.wallet = wallet
        self.song = song
        self.room = room
        self.tab = 0

    def pay_entry_fee(self, room):
        self.wallet -= room.fee
        self.tab += room.fee

    def buy_from_menu(self, order):
        self.wallet -= order.price
        self.tab += order.price

    def is_guest_skint(self, guest):
        if guest.wallet == 0:
            return "Skint!"
        return "Still loaded!"


class Rover:
    def __init__(self, position, karte):
        self.position = position
        self.karte = karte

    def up(self):
        self.bewege_nach(self.karte.position_oberhalb_von(self.position))

    def down(self):
        self.bewege_nach(self.karte.position_unterhalb_von(self.position))

    def left(self):
        self.bewege_nach(self.karte.position_links_von(self.position))

    def right(self):
        self.bewege_nach(self.karte.position_rechts_von(self.position))

    def bewege_nach(self, position):
        if self.karte.ist_frei(position):
            self.position = position

    def neue_karte(self, karte):
        self.karte = karte

    def steht_auf(self, position):
        return self.position == position

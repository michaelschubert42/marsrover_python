from Position import Position
import random


class Karte:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe
        self.hindernisse = set()
        self.wasser = set()

    def hindernisHinzufuegen(self, position):
        self.hindernisse.add(position)

    def hindernisHinzufuegenRandom(self, rover):
        x = random.randrange(0,self.breite+1)
        y = random.randrange(0,self.hoehe+1)
        position = Position(x,y)

        if rover.steht_auf(position):
            self.hindernisHinzufuegenRandom(rover)
        else:
            self.hindernisHinzufuegen(Position(x,y))

    def wasserHinzufuegen(self, position):
        self.wasser.add(position)

    def wasserHinzufuegenRandom(self, rover):
        x = random.randrange(0,self.breite+1)
        y = random.randrange(0,self.hoehe+1)
        position = Position(x,y)

        if rover.steht_auf(position) or position in self.hindernisse:
            self.wasserHinzufuegenRandom(rover)
        else:
            self.wasserHinzufuegen(Position(x,y))

    def ist_frei(self, position):
        return position not in self.hindernisse

    def position_oberhalb_von(self, position):
        return position.up() if self.enthaelt(position.up()) else Position(position.x, self.hoehe)

    def position_unterhalb_von(self, position):
        return position.down() if self.enthaelt(position.down()) else Position(position.x, 0)

    def position_links_von(self, position):
        return position.left() if self.enthaelt(position.left()) \
            else Position(self.breite, position.y)

    def position_rechts_von(self, position):
        return position.right() if self.enthaelt(position.right()) \
            else Position(0, position.y)

    def enthaelt(self, position):
        return 0 <= position.x <= self.breite and 0 <= position.y <= self.hoehe

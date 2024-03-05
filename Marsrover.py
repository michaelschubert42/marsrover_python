from tkinter import *

from Karte import Karte
from Position import Position
from Rover import Rover

BREITE = 1009
HOEHE = 700


def zeichne_oberflaeche():
    canvas.create_rectangle((3, 3), (BREITE + 1, HOEHE + 1), width=2, fill='brown')
    for zeile in range(1, 15):
        canvas.create_line((3, zeile * 50), (BREITE + 1, zeile * 50), width=2, fill='black')
    for spalte in range(1, 20):
        canvas.create_line((3 + spalte * 53, 3), (3 + spalte * 53, HOEHE + 1), width=2, fill='black')


def rover_bild():
    return PhotoImage(file='rover.png').subsample(12, 12)


def stein_bild():
    return PhotoImage(file='stone.png').subsample(21, 21)

def wasser_bild():
    return PhotoImage(file='water.png').subsample(10, 10)


def weihnachtsbaum_bild():
    return PhotoImage(file='weihnachtsbaum.png').subsample(6, 6)


rover_bild_id = 0
hindernis_bild_ids = set()
wasser_bild_id = 0


def platziere_rover_objekt(rover1):
    platziere_rover(rover1.position)


def platziere_rover(position):
    entferne_Rover()
    global rover_bild_id
    rover_bild_id = canvas.create_image(position.x * 53 + 7, position.y * 50 + 3, image=rover_bild, anchor='nw')


def platziere_hindernis(position):
    hindernis_bild_ids.add(
        canvas.create_image(position.x * 53 + 30, position.y * 50 + 23, image=stein_bild, anchor='center'))

def platziere_wasser(position):
    global wasser_bild_id
    wasser_bild_id = canvas.create_image(position.x * 53 + 30, position.y * 50 + 23, image=wasser_bild, anchor='center')

def entferne_Rover():
    canvas.delete(rover_bild_id)


def pfeil_nach_links_gedrueckt(rover):
    rover.left()
    platziere_rover_objekt(rover)


def pfeil_nach_rechts_gedrueckt(rover):
    rover.right()
    platziere_rover_objekt(rover)


def pfeil_nach_oben_gedrueckt(rover):
    rover.up()
    platziere_rover_objekt(rover)


def pfeil_nach_unten_gedrueckt(rover):
    rover.down()
    platziere_rover_objekt(rover)


def neue_karte_generieren():
    karte = Karte(18, 13)
    rover.neue_karte(karte)
    loesche_Hindernisse()
    loesche_Wasser()

    platziere_rover_objekt(rover)

    for i in range(50):
        karte.hindernisHinzufuegenRandom(rover)

    for hindernis in karte.hindernisse:
        platziere_hindernis(hindernis)

    karte.wasserHinzufuegenRandom(rover)

    for wasser in karte.wasser:
        platziere_wasser(wasser)


def loesche_Hindernisse():
    for bild_id in hindernis_bild_ids:
        canvas.delete(bild_id)
    hindernis_bild_ids.clear()

def loesche_Wasser():
    canvas.delete(wasser_bild_id)

fenster = Tk()
fenster.geometry("1200x800")
label = Label(fenster, text="Marsrover")
label.pack()

rover_bild = rover_bild()
stein_bild = stein_bild()
weihnachtsbaum_bild = weihnachtsbaum_bild()
wasser_bild = wasser_bild()

canvas = Canvas(fenster, width=BREITE, height=HOEHE, bg='brown')
canvas.pack(anchor=CENTER, expand=True)

neueKarte = Button(fenster, text="Neue Karte", command=neue_karte_generieren)
neueKarte.pack()

zeichne_oberflaeche()
karte = Karte(18, 13)
rover = Rover(Position(3, 4), karte)

platziere_rover_objekt(rover)

for i in range(50):
    karte.hindernisHinzufuegenRandom(rover)

karte.wasserHinzufuegenRandom(rover)

for hindernis in karte.hindernisse:
    platziere_hindernis(hindernis)

for wasser in karte.wasser:
    platziere_wasser(wasser)

fenster.bind("<Down>", lambda _: pfeil_nach_unten_gedrueckt(rover))
fenster.bind("<Right>", lambda _: pfeil_nach_rechts_gedrueckt(rover))
fenster.bind("<Up>", lambda _: pfeil_nach_oben_gedrueckt(rover))
fenster.bind("<Left>", lambda _: pfeil_nach_links_gedrueckt(rover))

button = Button(fenster, text="Schliessen", command=fenster.destroy)
button.pack()
fenster.mainloop()

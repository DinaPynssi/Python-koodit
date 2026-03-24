"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina
kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan
ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

1. tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
2. tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
3. kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa
eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein
sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

"""

import random
from operator import truediv

from mysql.connector.constants import flag_is_set


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdytä(self,muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus :
            self.nopeus = self.huippunopeus
        if self.nopeus < 0 :
            self.nopeus = 0
    def kulje(self, tunnit):
        self.matka += (tunnit * self.nopeus)


class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat
    def tunti_kuluu(self):
        for auto in self.osallistujat:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print()

    def kilpailu_ohi(self):
        loppu = False
        while True:
            if loppu == True



autot = []
for i in range(1, 11):
    rekisteritunnus = "ABC" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

loppu = False

while True:
    if loppu == True:
        break
    for auto in autot:
        if auto.matka > 10000:
            loppu = True
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

for auto in autot:
    print(f"Rekisterinumero {auto.rekisteritunnus}, kuljettu matka {auto.matka}")


auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)


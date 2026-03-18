#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus
# ja kuljettu matka. Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)

print(f"Auton ominaisuudet ovat: rekisteritunnus {auto.rekisteritunnus}, huippunopeus {auto.huippunopeus} km/h, auton tämänhetkinen nopeus {auto.nopeus} ja matka tällä hetkellä {auto.matka}")

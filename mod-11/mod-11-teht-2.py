"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat:
Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat.
Esimerkiksi sähköauton alustaja saa parametreinaan:
rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
"""

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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)

#pääohjelma

sähkoauto1 = Sähköauto("ABC-15",180, 52.2)
polttomoottoriauto1 = Polttomoottoriauto("ACD-123", 165, 32.3)


sähkoauto1.kiihdytä(100)
polttomoottoriauto1.kiihdytä(130)

sähkoauto1.kulje(3)
polttomoottoriauto1.kulje(3)

print(f"Sähköauton matka: {sähkoauto1.matka} km")
print(f"Polttomoottoriauton matka: {polttomoottoriauto1.matka} km")



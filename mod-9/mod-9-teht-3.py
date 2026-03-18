#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on
# tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)

auto.matka= 2000
auto.nopeus = 60
auto.kulje(1.5)

print(f"{auto.matka}")

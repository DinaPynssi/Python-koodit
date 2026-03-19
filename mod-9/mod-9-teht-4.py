#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten,
# että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


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


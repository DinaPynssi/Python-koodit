"""
Jatka edellisen tehtävän ohjelmaa siten,
että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

"""


class Hissi:
    def __init__(self, alin = 1, ylin = 10):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = self.alin

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"{self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"{self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros != kerros:
            if self.nykyinen_kerros < kerros:
                self.kerros_ylös()
            else: self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, kerrosten_lkmr):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(kerrosten_lkmr):
            self.hissit.append(Hissi(alin,ylin))

    def aja_hissiä(self, nro, kohdekerros):
        self.hissit[nro].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


#pääohjelma

talo = Talo(alin=1, ylin=10, kerrosten_lkmr=3)
talo.aja_hissiä(0,5)
talo.palohälytys()

"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.
siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
 ja sen jälkeen takaisin alimpaan kerrokseen.

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


#pääohjelma
h = Hissi(1,10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)





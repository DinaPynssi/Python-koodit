#muokkaa edellisstä funktiota niin, että funktio saa parametrinä nopan
#tahkojen yhteismäärän. nopan heittoa jatketaan pääohjelmanssa kunnes
#saadaan nopan maksimisilmäluku jota kysytään käyttäjältä ohjelman suorituksen alussa

import random
def noppa(lkmr):
    return random.randint(1, lkmr)

lkmr = int(input("anna tahkojen lukumäärä: "))

heitot = noppa(lkmr)
while heitot != lkmr:
    print(f'{heitot}')
    print("heitetään uudestaan")
    heitot = noppa(lkmr)
if heitot == lkmr :
    print(f'{heitot}')
    print(f"sait {heitot}, ohjelma loppuu")

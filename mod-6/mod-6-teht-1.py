#kirjoita parametriton funktio, joka palauttaa paluuarvona satunnaisen nopan
#silmäluvun väliltä 1-6. Kirjoita pääohjelma joka heittää noppaa niin kauan
#kunnes tulee kutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun

import random
def noppa():
    return random.randint(1,6)

heitot = noppa()
while heitot < 6 :
    print(f'{heitot}')
    print("heitetään uudestaan")
    heitot = noppa()
print("Sait kutosen, ohjelma loppuu")




# tässä tehtävässä ei tarvita tuota iffiä koska voidaan myös vaan käyttää whilessä raja-arvoa 6







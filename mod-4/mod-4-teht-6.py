# pii = 4n/N
# n = x**2 + y**2 < 1
# Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä
# toteuttaa piin likiarvon laskennan edellä kuvatulla menetelmällä.
# Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle.

import random
from random import randint

N = int(input("Arvottavien pisteiden määrä: "))
piste = 0
n = 0
while piste < N :
    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1 :
        n = n+1
    piste = piste+1
Pii = 4*n / N
print(Pii)




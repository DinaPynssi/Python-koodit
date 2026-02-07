#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

koodi1 = random.randint (0,9), random.randint(0,9), random.randint(0,9)

koodi2 = random.randint(1,6), random.randint (1,6), random.randint (1,6), random.randint (1,6)

print(koodi1, koodi2)





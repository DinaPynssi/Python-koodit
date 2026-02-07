#kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta.alan
#ympyrän A on A = pii * r ^2

import math
sade = float(input("Anna ympyrän säde: "))
pinta_ala = math.pi * sade ** 2
print("Ympyrän pinta-ala on", pinta_ala)


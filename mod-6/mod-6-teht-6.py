#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat
# sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pitsa (halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija / 2) ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

Pitsa1_halkaisija = float(input("Pitsan halkaisija: "))
Pitsa1_hinta = float(input("Pitsan hinta euroina: "))
yksikkohinta1 = pitsa(Pitsa1_halkaisija,Pitsa1_hinta)

Pitsa2_halkaisija = float(input("Pitsan halkaisija: "))
Pitsa2_hinta = float(input("Pitsan hinta euroina: "))
yksikkohinta2 = pitsa(Pitsa2_halkaisija,Pitsa2_hinta)

if yksikkohinta1 < yksikkohinta2 :
    print(f"Ensimmäisen pitsan yksikköhinta on {yksikkohinta1:.2f}, ja siinä on parempi vastine rahalle")
else:
    print(f"Toisen pitsan yksikköhinta on {yksikkohinta2:.2f}, ja siinä on parempi vastine rahalle")







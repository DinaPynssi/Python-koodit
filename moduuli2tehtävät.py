nimi= input('Anna nimesi: ')
print("Terve, " + nimi+ "!")

import math
sade = float(input("Anna ympyrän säde:"))
pinta_ala = math.pi * sade ** 2
print("Ympyrän pinta-ala on: ", pinta_ala)

kanta_str = input("Anna suorakulmion kanta")
kanta = float(kanta_str)
korkeus_str = input("Anna suorakulmion korkeus")
korkeus = float(korkeus_str)
Pinta_ala = kanta * korkeus
Piiri = kanta * 2 + korkeus * 2
print("Suorakulmion pinta-ala ja piiri ovat: " , Pinta_ala, Piiri)

print("Anna kolme kokonaislukua")
eka_str = input('Eka: ')
eka = float(eka_str)
toka_str = input('Toka: ')
toka = float(toka_str)
kolmas = input('Kolamas: ')
kolmas = float(kolmas)

summa = eka + toka + kolmas
tulo = eka * toka * kolmas
keskiarvo = eka * toka * kolmas / 3
print("Lukujen summa, tulo ja keskiarvo ovat: " , summa , tulo , keskiarvo)
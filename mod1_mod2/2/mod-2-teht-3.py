#kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden
#ohjelma tulostaa suorakulmion piirin ja pinta-alan

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = kanta * 2 + korkeus * 2
pinta_ala = kanta * korkeus

print("Suorakulmion piiri on", piiri)
print("Suorakulmion pinta-ala on", pinta_ala)


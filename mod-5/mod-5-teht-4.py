#kirjoita ohjelma joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# käytä for toistorakennetta nimen kysymiseen
# tallenna nimet listarakenteeseen
# lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin
# ne syötettiin. käytä for toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen


kaupungit = []

for i in range (5) :
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

for kaupunki in kaupungit:
    print(f"{kaupunki}")


#kirjoita funktio joka saa parametrinä bensiinin määrän nestegallonoina
#ja palauttaa paluuarvonaan vastaavan litramäärän
#kirjooitetaan pääohjelma joka kysyy gallonamäärän ja muuntaa sen litroiksi
#muutos tehdään aliohjelmalla
#muuntoa jatketaan kunnes käyttäjä antaa neg. gallonamäärän
#1 gallona on 3,785 litraa


def gallona(maara):
    return maara * 3.785


maara = float(input("Kuinka monta gallonaa: "))
while maara > 0 :
    litrat = gallona(maara)
    print(f" {maara} gallonaa on litroina {litrat}")
    maara = float(input("Kuinka monta gallonaa: "))




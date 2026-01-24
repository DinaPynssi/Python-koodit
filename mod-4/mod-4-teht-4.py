# kirjoita peli jossa tietokone arpoo kokonaisluvun väliltä 1..10
# kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein
# kunkin arvauksen jälkeen ohjelma tulostaa: liian suuri arvaus, liian pieni arvaus
# tai oikein
# tietokone ei saa vaihtaa lukua arvauskertojen välissä
import random

arvaus = int(input("Anna luku: "))
luku = random.randint(1,10)
while arvaus != luku :
    if arvaus > luku :
        print("Liian suuri arvaus")
        arvaus = int(input("Anna uusi arvaus: "))
    elif arvaus < luku :
        print("Liian pieni arvaus")
        arvaus = int(input("Anna uusi arvaus: "))
print("Oikein")



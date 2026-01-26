#kirjoita ohjelma joka kysyy käyttäjältä arpakuutioiden(noppien) lukumäärän
# ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan
# käytä for-toistorakennetta

import random

lkm = int(input("Noppien määrä: "))
summa = 0
#esitellään muuttuja johon voidaan laskea noppien silmälukujen summa
#asetetaan alkuarvoksi nolla

for nopan_nro in range (lkm):
    #heitetään noppia haluttu lkmr
    #muuttuja nopan_nro on ns kierroslaskuri. Sen arvo alkaa nollasta.
    silmaluku = random.randint(1,6)
    #lisätään saatu silmäluku muuttujan summan arvoon
    summa += silmaluku
    # += on lyhennys tästä -> summa = summa + silmäluku
    # näitä lyhennyksiä on myös esim. -= -> summa = summa - silmäluku jne.
    # moduuli 2 nämä lyhennykset
    print(f"noppa{nopan_nro}, silmäluku = {silmaluku}")
    #toi ylempi on xtra jotta voidaan tarkistaa kun tulostetaan saatu silmäluku

#tulostetaan noppien silmälukujen summa
print(f"Silmälukujen summa = {summa}")




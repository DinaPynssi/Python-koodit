#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
#ja tulostat sen palauttaman summan.


def lista(luvut) :
    summa = 0
    for i in luvut :
        summa += i
    return summa

lukulista = [2,6,3,2,6]
lukusumma = lista(lukulista)
print(lukusumma)



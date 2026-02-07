#kirjoita ohjelma joka kysyy kolme kokonaislukua
#ohjelma tulostaa lukujen summan tulon ja keskiarvon

eka = int(input("Anna kokonaisluku: "))
toka = int(input("Anna toinen: "))
kolmas = int(input("Anna kolmas: "))

summa = eka + toka + kolmas
tulo = eka * toka * kolmas
keskiarvo = eka + toka + kolmas / 3

print("Lukujen summa, tulo ja keskiarvo ovat", summa, tulo, keskiarvo)


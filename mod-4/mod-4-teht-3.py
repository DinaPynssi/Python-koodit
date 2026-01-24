#kirjoita ohjelma joka kysyy käyttäjältä lukuja siihen saakka
# kunnes hän syöttää tyhjän merkkijonon lopetusmerkiksi
#lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman
from enum import pickle_by_enum_name
silmukassa = False
luku_str = input("Anna luku: ")
if luku_str != "":
    luku_int = int(luku_str)
    suurin = luku_int
    pienin = luku_int
    silmukassa = True
else:
    print("lopetit heti")

while luku_str != "" :
    if luku_int > suurin :
        suurin = luku_int
    if luku_int < pienin :
        pienin = luku_int
    luku_str = input("Anna luku: ")
    if luku_str != "":
        luku_int = int(luku_str)
if silmukassa == True:
    print(f' {pienin} {suurin}')


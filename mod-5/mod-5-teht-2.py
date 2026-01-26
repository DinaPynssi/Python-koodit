#ohjelma kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
#lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä
#suurimmasta alkaen
#lajittelujärjestyksen voi kääntää anatamalla sort -metodille argumentiksi
# reverse = true
from operator import truediv

lista = []
luku = input("Anna luku: ")
while luku != "" :
    lista.append(int((luku)))
    luku = input("Anna luku: ")

lista.sort(reverse=True)

for luku in lista [:5] :
    print(luku)



#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko :
# tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimi = set()
anna_nimi = input("Anna nimi: ")

while anna_nimi != "" :
    if anna_nimi in nimi :
        print("Aiemmin annettu nimi")
        anna_nimi = input("Anna uusi nimi: ")
    else:
        nimi.add(anna_nimi)
        anna_nimi = input("Anna uusi nimi: ")



for i in nimi :
    print(i)





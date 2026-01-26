#kirjoita ohjelma joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa
#onko se alkuluku
#alkulukuja ovat jaollisia vain ykkösellä ja itsellään
#esim 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 niin et se menee tasan
#mut sit esim 21 ei oo alkuluku, koska se voidaan jakaa myös luvulla 3 ja 7

luku = int(input("Anna kokonaisluku:"))
jakaja = 2
on_alkuluku = True

for jakaja in range (2, luku) :
    if luku % jakaja == 0 :
        on_alkuluku = False

if on_alkuluku == True :
    print("On alkuluku")
else :
    print("Ei ole alkuluku")




#ohjelma kysyy käyttäjältä käyttäjätunnuksen ja salasanan
# jos jompikumpi TAI molemmat on väärin, ne kysytään uudelleen
# jompikumpi tai molemmat -> OR
# tätä jatketaan kunnes kirj. tiedot on oikein TAI väärät tiedot on syötetty 5 krt
# Jos oikein - tulostetaan "Tervetuloa"
# Jos 5 krt väärin tulostetaan "Pääsy evätty"
# käyttäjätunnus on = python ja salasana = rules

kayttaja = input("Anna käyttäjätunnus: ")
salis = input("Anna salasana: ")
kerrat = 1

while (kayttaja != "python" or salis != "rules") and kerrat < 5 :
    kayttaja = input("Anna käyttäjätunnus: ")
    salis = input("Anna salasana: ")
    kerrat = kerrat +1

if kayttaja == "python" and salis == "rules" :
    print("Tervetuloa")
else :
    print("Pääsy evätty")





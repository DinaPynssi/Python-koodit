#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


#jaetaan koodi eri funktioihin
#avaimena on ICAO koodi! tämän takia lisaamis funktiossa arvo on nimi, koska avain on koodi
# niin arvo on nimi

def lisaa() :
    #funktio lisää uuden lentokentän sanakirjaan
    nimi = input("Anna lentokentän nimi:")
    koodi = input("Anna lentokentän ICAO-koodi:")
    lentoasemat[koodi]=nimi

def hae():
    koodi = input("Anna lentokentän ICAO-koodi:")
    if koodi in lentoasemat:
        print(f"Lentoaseman {koodi} nimi on {lentoasemat[koodi]} ")


def tulosta_valikko():
    #funktio tulostaa käyttäjälle eri vaihtoehdot
    print("Valitse toiminto:")
    print("1 = Lisää uusi lentoasema")
    print("2 = Hae lentoaseman tiedot ")
    print("3 = lopeta")

#kirjoitetaan pääohjelma


#luodaan snaakirjan lentokentän tietoja varten
lentoasemat = {
    "EFHK" : "Helsinki-Vantaa"

}

toiminto = 0 #käyttäjän valitsema toiminnon nro

while toiminto != 3 :
    tulosta_valikko()
    toiminto = int(input("Valitse toiminto:"))
    if toiminto == 1 :
        lisaa()
    elif toiminto == 2 :
        hae()
    else:
        "Tuntematon toiminto"

print("Lopetit ohjelman")

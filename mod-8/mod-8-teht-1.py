#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
#Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
#kurssilla käytettävästä lentokenttätietokannasta.
#ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

def hae_icao(ident):
    sql = f"SELECT name, municipality FROM airport where ident = '{ident}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokenttä jonka ICAO koodi on {ident} on nimeltään {rivi[0]}. Kyseinen lentokenttä sijaitsee kunnassa {rivi[1]} ")



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='JAAJOmaria23',
         autocommit=True
         )

koodi = input("Anna lentokentän ICAO-koodi: ")
hae_icao(koodi)



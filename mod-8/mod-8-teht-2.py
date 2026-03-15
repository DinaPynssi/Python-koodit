#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
#ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
#Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
#että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

def hae_maa(iso_country):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{iso_country}' group by type"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[1]} {rivi[0]}")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='JAAJOmaria23',
         autocommit=True
         )

maakoodi = input("Anna maakoodi: ")
hae_maa(maakoodi)

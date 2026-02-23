#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
#Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
#Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
#Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
#Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.



import mysql.connector
from geopy.distance import geodesic

def hae_etaisyys(iso_country) :
    sql = f" SELECT "


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='JAAJOmaria23',
         autocommit=True
         )


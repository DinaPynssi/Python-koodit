import mysql.connector

#alempana rivillä 7 huomioi merkit. " on ympärillä koska se on python kieltä. ja sitten  '{iso_country}'
#on noissa pikkuheittomerkeissä koska sql:sä pitää olla heittomerkit noissa nimissä kun käsketään jtn.

def hae_maa(iso_country):
    sql = f"SELECT name, continent FROM country where iso_country ='{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Lentokenttä jonka iso_country koodi on {iso_country} sijaitsee maassa {rivi[0]}. Kyseinen maa sijaitsee maanosassa: {rivi[1]}")


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='JAAJOmaria23',
         autocommit=True
         )

hae_maa("FI")

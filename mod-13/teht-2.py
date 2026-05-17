"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän
ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
 Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
 Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
 http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
 {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

"""
from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='SALASANAA EN LAITA TÄHÄ KU JULKINE REPO',
    autocommit=True
)

@app.route('/kenttä/<icao>')
def airport(icao):

    cursor = conn.cursor()

    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"

    cursor.execute(sql)

    result = cursor.fetchone()

    response = {
        "ICAO": icao,
        "Name": result[0],
        "Municipality": result[1]
    }

    return Response(
        json.dumps(response),
        mimetype="application/json"
    )

app.run(host='127.0.0.1', port=3000)ader=True, host='127.0.0.1', port=3000)
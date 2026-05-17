"""

Tutustu avoimeen OpenWeather-säärajapintaan:
https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi.
Palveluun rekisteröityminen on tarpeen,
jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.


"""

import requests

api_avain = "OMA_API_AVAIN"

paikkakunta = input("Anna paikkakunta: ")

saa = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&units=metric"
).json()

print(saa["weather"][0]["description"])
print(f"{saa['main']['temp']} °C")
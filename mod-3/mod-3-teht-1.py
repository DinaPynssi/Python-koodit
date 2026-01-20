#kysytään kalastajalta kuhan pituus senttimetreinä
# jos kuha alamittainen, ohjelma käskee laskea takas järveen ja ilmoittaa käyttäjälle
# montako sivua alimmasta sallitusta pyyntimitasta puuttuu
# alimittainen jos alle 37 cm

pituus = float(input("Anna kuhan pituus senttimetreinä: "))
if pituus < 37 :
    print("Laske kuha takaisin järveen")
    print(f'Kuha on {37 - pituus} alimittainen')
elif pituus > 37 :
    print("Onnea kalasaaliista")


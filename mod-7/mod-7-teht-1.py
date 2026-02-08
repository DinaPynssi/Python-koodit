#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.
# tässä tehtävässä luodaan monikko

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukauden_numero = int(input("Anna kuukauden numero (1-12): "))
kuukausi = vuodenajat[kuukauden_numero-1]
print(f"{kuukauden_numero} on {kuukausi}")







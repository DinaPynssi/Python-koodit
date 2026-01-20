# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.



sukupuoli = input("Sukupuoli: ")
if sukupuoli == "nainen" :
    hemoglobiini = int(input("Hemoglobiini: "))
    if sukupuoli == "nainen" and 117<=hemoglobiini<=175 :
        print("Normaali hemoglobiiniarvo")
    elif hemoglobiini < 117 :
        print("Alhainen hemoglobiini")
    elif hemoglobiini > 175 :
            print("Korkea hemoglobiini")
if sukupuoli == "mies" :
    hemoglobiini = int(input("Hemoglobiini: "))
    if sukupuoli == "mies" and 134<=hemoglobiini<=195 :
        print("Normaali hemoglobiiniarvo")
    elif hemoglobiini < 134 :
        print("Alhainen hemoglobiini")
    elif hemoglobiini > 195 :
        print("Korkea hemoglobiini")



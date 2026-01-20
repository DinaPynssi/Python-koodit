# ohjelma kysyy vuosiluvun, ja ilmoittaa onko annettu vuosi karkausvuosi
# jos vuosi on jaollinen 400:lla - on karkausvuosi
# muuten jos vuosi on jaollinen 100:lla - ei ole
# muuten jos vuosi on jaollinen 4:lla - on karkausvuosi
# muuten - ei ole

# if
# elif
# else
# rakenne
# TAi yhden rivin rakenne or - rakenteella
# IF on jaollinen 400:lla TAI (IS NOT jaollinen 100:lla JA on jaollinen 4:lla) - on karkausvuosi
# Else: ei ole

vuosi = int(input("Anna vuosiluku: "))
if vuosi % 400 == 0 or vuosi % 100 != 0 and vuosi % 4 == 0 :
    print("On karkausvuosi")
else:
    print("Ei ole karkausvuosi")




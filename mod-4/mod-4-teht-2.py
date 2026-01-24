# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = int(input("Anna tuumat: "))
while tuumat > 0 :
    sentit = tuumat * 2.54
    print(f'Senttimetreinä on {sentit}')
    tuumat = int(input("Anna tuumat: "))



#sentit = tuumat * 2,54
#while tuumat <= 0 :
    #print("Anna positiivinen luku")
    #break
#if tuumat > 0 :
    #sentit = (tuumat * 2.54)
    #print(f'{sentit}')





#kirjoita ohjelma joka kysyy massan keskiaikaisten mittojen mukaan leivisköinä nauloina ja luoteina
#ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa käyttäjälle tuloksen
# 1 leiviskä = 20 naulaa
# 1 naula = 32 luotia
# 1 luoti = 13,3 grammaa

leiviskat = (input("Anna leiviskät: "))
leiviskat_float = float(leiviskat)
naulat = (input("Anna naulat: "))
naulat_float = float(naulat)
luodit = (input("Anna luodit: "))
luodit_float = float(luodit)

luodit_yht = (leiviskat_float * 20 * 32) + (naulat_float * 32) + luodit_float
grammat_float = luodit_yht * 13.3
kilot = int(grammat_float / 1000)
#yli jää grammoiksi
grammat2 = grammat_float % 1000

print(f"Massa nykymittojen mukaan: {kilot} kiloa ja {grammat2:.2f} grammaa.")



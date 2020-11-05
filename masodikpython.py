"""
Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a
képernyőre eddig a számig, egymástól szóközzel elválasztva
eddig = 12

szoveg = "0"

for x in range(1, eddig + 1):
	szoveg = szoveg + " " + str(x)

print(szoveg)
"""
"""
egymás alá
"""
eddig = 12


for x in range(-12, eddig + 1, 3):
	print(x)


#8.	Tárolj el két számot egy-egy változóba! Egy harmadik változóba tárold el a két szám szorzatát, majd írasd ki a képernyőre!

import szamkero

def nyolcasFeladat ():

    szam1 = szamkero.beolvas()
    szam2 = szamkero.beolvas()
    szam3 = szamkero.beolvas()
    szorzat = (szam1 * szam2 * szam3)

    print("A három szám szorzata: "+str(szorzat)+" .")
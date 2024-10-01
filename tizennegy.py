# 14. Tárolj el 3 számot egy-egy változóba! Írd ki a számtani közepüket!

import szamkero

def tizennegyFeladat ():

    szam1 = szamkero.beolvas()
    szam2 = szamkero.beolvas()
    szam3 = szamkero.beolvas()
    szamtanikozep = ((szam1 + szam2 + szam3)/3)

    print("A három szám számtani közepe: "+str(szamtanikozep)+" .")
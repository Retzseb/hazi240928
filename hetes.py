# 7. Tárolj el két számot egy-egy változóba! Írd ki az osztási maradékukat.

import szamkero

def hetesFeladat ():

    szam1 = szamkero.beolvas()
    szam2 = szamkero.beolvas()
    maradek = (szam1 % szam2)

    print("A két szám osztási maradéka: "+str(maradek)+" .")
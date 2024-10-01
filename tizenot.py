# 15. Tárolj el 3 számot egy-egy változóba! Írd ki a középső számot az értékük szerint összehasonlítva!
from debugpy.launcher.winapi import kernel32

import szamkero

def tizenotFeladat ():

    szam1 = szamkero.beolvas()
    szam2 = szamkero.beolvas()
    szam3 = szamkero.beolvas()
    if szam1 < szam2 < szam3:
        print("A második szám értéke a középső")
    elif szam2 < szam1 < szam3:
        print("Az első szám értéke a középső")
    else:
        print("A harmadik szám értéke a középső")

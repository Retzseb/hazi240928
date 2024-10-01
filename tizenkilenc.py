# 19. Tárolj el egy kétjegyű egész számot egy változóba! Írd ki a számjegyek összegét!

def beolvas():
    szam = int(input("Kérem adjon meg egy kétjegyű számot!"))
    return szam

def tizenkilencFeladat():
    szam = beolvas()
    tizes = (szam // 10)
    egyes = (szam % 10)
    szamjegy = (tizes+egyes)

    print("A számjegyek összege: "+str(szamjegy)+" .")

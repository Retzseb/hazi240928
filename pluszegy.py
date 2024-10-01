#Keress a w3schholson egy olyan python függvényt, amivel tudod ellenőrizni hogy egy adat átalakítható-e általam akart típussá. (kimenete: logikai érték)

def beolvas():
    adat = input("Kérem adjon meg egy adatot! ")
    return adat

def beolvas2():
    tipus = input("Kérem adjon meg egy típust! ")
    return tipus

def pluszKonvert(adat, tipus):
    try:
        tipus(adat)
        return True
    except (ValueError, TypeError):
        return False

adat = beolvas()
tipus = beolvas2()

if tipus == "int":
    tipus_fuggveny = int
elif tipus == "float":
    tipus_fuggveny = float
elif tipus == "str":
    tipus_fuggveny = str
else:
    print("Nem támogatott típus!")
    tipus_fuggveny = None

if tipus_fuggveny:
    eredmeny = pluszKonvert(adat, tipus_fuggveny)
    print(f"Átalakítható: {eredmeny}")

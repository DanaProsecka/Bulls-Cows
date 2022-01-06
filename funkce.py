def zvaliduj_vstup(zadane_cislo):
    if zadane_cislo.startswith("0"):
        print("Zadane cislo musí mít 4 znaky a nesmi zacinat 0!")
        return False

    try:
        int(zadane_cislo)
    except Exception:
        print("Neplatne cislo!")
        return False

    if len(zadane_cislo) != 4:
        print("Zadane cislo musí mít 4 znaky!")
        return False

    for pismeno in zadane_cislo:
        if zadane_cislo.count(pismeno) > 1:
            print("Cislice se opakuji!")
            return False

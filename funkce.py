def zvaliduj_vstup(zadane_cislo):
    if zadane_cislo.startswith("0"):
        print("Number must not begin with 0!")
        return False

    try:
        int(zadane_cislo)
    except Exception:
        print("Invalid number!")
        return False

    if len(zadane_cislo) != 4:
        print("The number entered must be 4 digits long!")
        return False

    for pismeno in zadane_cislo:
        if zadane_cislo.count(pismeno) > 1:
            print("Numbers are repeating, try again!")
            return False

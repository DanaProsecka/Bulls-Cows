import random
from funkce import zvaliduj_vstup

oddelovac = "-" * 30

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(oddelovac)

print(oddelovac)
cisla = "123456789"
vysledne_cislo = ""


while len(vysledne_cislo) < 4:
    cislo = random.choice(cisla)
    index = vysledne_cislo.find(cislo)
    if index < 0:
        vysledne_cislo += cislo

print(vysledne_cislo)
pokusy = 0
while True:
    pokusy = pokusy + 1
    zadane_cislo = input("Enter a number: ")

    if zvaliduj_vstup(zadane_cislo) is False:
        continue

    if vysledne_cislo == zadane_cislo:
        print("Correct, you've guessed the right number!")
        print("Pocet pokusu ", pokusy)
        exit(0)

    cows = 0
    bulls = 0
    for pismeno in zadane_cislo:
        # index_z = zadane_cislo.find(pismeno)
        index_v = vysledne_cislo.find(pismeno)
        if index_v >= 0:
            index_z = zadane_cislo.find(pismeno)
            if index_z == index_v:
                bulls = bulls + 1
            else:
                cows = cows + 1

    print(str(bulls) + (" bull," if bulls == 1 else " bulls, ") + str(cows) + (" cow" if cows == 1 else " cows"))

    #print(f"Bulls, {bulls}, Cows {cows}")

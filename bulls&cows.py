import random
from funkce import zvaliduj_vstup

oddelovac = "-" * 48

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

#print(vysledne_cislo)
pokusy = 0
while True:
    pokusy = pokusy + 1
    zadane_cislo = input("Enter a number: ")

    if zvaliduj_vstup(zadane_cislo) is False:
        continue

    if vysledne_cislo == zadane_cislo:
        print("Correct, you've guessed the right number!")
        print("Number of guesses: ", pokusy)
        if pokusy < 3:
            print("That's amazing!")
        elif pokusy < 7:
            print("That's average..")
        else:
            print("That's not good, you can do better!")
        exit(0)

    cows = 0
    bulls = 0
    for i in zadane_cislo:
        index_v = vysledne_cislo.find(i)
        if index_v >= 0:
            index_z = zadane_cislo.find(i)
            if index_z == index_v:
                bulls = bulls + 1
            else:
                cows = cows + 1

    print(str(bulls) + (" bull," if bulls == 1 else " bulls, ") + str(cows) + (" cow" if cows == 1 else " cows"))



import random

def jugar():
    monedas = 10
    jugando = True

    print("Welcome to Lucky Dice!")
    print("Bet coins and guess the sum of two dice:")
    print("Choose a low sum (2-6), seven or a high sum (8-12) and roll the dice.")
    print("Low and high pay what you bet. Seven pays triple.")

    while jugando and monedas > 0:
        print("")
        print("You have " + str(monedas) + " coins")

        pidiendo_apuesta = True
        while pidiendo_apuesta:
            try:
                apuesta = int(input("How many coins do you want to bet? "))
                if apuesta < 1:
                    print("You have to bet at least 1 coin.")
                elif apuesta > monedas:
                    print("You can't bet more than you have (" + str(monedas) + ").")
                else:
                    pidiendo_apuesta = False
            except ValueError:
                print("That is not a whole number, try again.")

        pidiendo_eleccion = True
        while pidiendo_eleccion:
            eleccion = input("Choose low, seven or high: ").lower().strip()
            if eleccion == "low" or eleccion == "seven" or eleccion == "high":
                pidiendo_eleccion = False
            else:
                print("Invalid option. Type exactly: low, seven or high.")

        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        suma = dado_1 + dado_2
        print("You rolled " + str(dado_1) + " and " + str(dado_2) + ": sum " + str(suma))

        if eleccion == "low" and suma < 7:
            print("You won " + str(apuesta) + " coins!")
            monedas = monedas + apuesta
        elif eleccion == "high" and suma > 7:
            print("You won " + str(apuesta) + " coins!")
            monedas = monedas + apuesta
        elif eleccion == "seven" and suma == 7:
            print("Exactly seven! You won " + str(apuesta * 3) + " coins")
            monedas = monedas + apuesta * 3
        else:
            print("You lost " + str(apuesta) + " coins")
            monedas = monedas - apuesta

        if monedas > 0:
            pidiendo_seguir = True
            while pidiendo_seguir:
                otra = input("Keep playing? (y/n): ").lower().strip()
                if otra == "y":
                    pidiendo_seguir = False
                elif otra == "n":
                    pidiendo_seguir = False
                    jugando = False
                else:
                    print("Type only y or n.")

    if monedas <= 0:
        print("You ran out of coins. Game over!")
    else:
        print("You left with " + str(monedas) + " coins.")
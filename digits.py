import random

def jugar():
    numero_secreto_1 = random.randint(1, 50)
    numero_secreto_2 = random.randint(1, 100)
    numero_secreto_3 = random.randint(1, 500)

    maximo_intentos = 10
    contador_intentos = 0
    adivinado = False

    print("Welcome to Guess the Number!")
    print("Choose a difficulty")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    opcion = input("Choose an option: ")

    if opcion == "1":
        while not adivinado and contador_intentos < maximo_intentos:
            correcto = True
            while correcto:
                try:
                    intento = int(input("Enter a number: "))
                    correcto = False
                except ValueError:
                    print("That is not a number, try something else.")
            contador_intentos = contador_intentos + 1

            if intento < numero_secreto_1:
                print("The number is higher")
            elif intento > numero_secreto_1:
                print("The number is lower")
            else:
                print("Congratulations! You found the secret number")
                adivinado = True
        if adivinado:
            print("You did it in: " + str(contador_intentos) + " attempts.")
        else:
            print("You ran out of attempts. The number was " + str(numero_secreto_1))

    elif opcion == "2":
        while not adivinado and contador_intentos < maximo_intentos:
            correcto = True
            while correcto:
                try:
                    intento = int(input("Enter a number: "))
                    correcto = False
                except ValueError:
                    print("That is not a number, try something else.")
            contador_intentos = contador_intentos + 1

            if intento < numero_secreto_2:
                print("The number is higher")
            elif intento > numero_secreto_2:
                print("The number is lower")
            else:
                print("Congratulations! You found the secret number")
                adivinado = True
        if adivinado:
            print("You did it in: " + str(contador_intentos) + " attempts.")
        else:
            print("You ran out of attempts. The number was " + str(numero_secreto_2))

    elif opcion == "3":
        while not adivinado and contador_intentos < maximo_intentos:
            correcto = True
            while correcto:
                try:
                    intento = int(input("Enter a number: "))
                    correcto = False
                except ValueError:
                    print("That is not a number, try something else.")
            contador_intentos = contador_intentos + 1

            if intento < numero_secreto_3:
                print("The number is higher")
            elif intento > numero_secreto_3:
                print("The number is lower")
            else:
                print("Congratulations! You found the secret number")
                adivinado = True
        if adivinado:
            print("You did it in: " + str(contador_intentos) + " attempts.")
        else:
            print("You ran out of attempts. The number was " + str(numero_secreto_3))
    else:
        print("That option doesn't exist, try a number from 1 to 3")
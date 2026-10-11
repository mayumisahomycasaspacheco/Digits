import random
import time

def jugar():
    largo = 3
    mejor = 0
    jugando = True

    print("")
    print("=== DIGIT MEMORY ===")
    print("You will see a sequence of numbers for a few seconds.")
    print("Memorize it and type it. Every round will have one more digit.")
    print("")
    input("Press Enter to start...")

    while jugando:
        secuencia = ""
        i = 0
        while i < largo:
            secuencia = secuencia + str(random.randint(0, 9))
            i = i + 1

        print("")
        print("Memorize: " + secuencia)
        time.sleep(1 + largo * 0.5)
        print("\n" * 40)

        pidiendo = True
        while pidiendo:
            respuesta = input("What was the sequence? ").strip()
            if not respuesta.isdigit():
                print("Type only digits, no letters or spaces.")
            elif len(respuesta) != largo:
                print("The sequence had " + str(largo) + " digits.")
            else:
                pidiendo = False

        if respuesta == secuencia:
            print("Correct!")
            mejor = largo
            largo = largo + 1
        else:
            print("Wrong, it was " + secuencia)
            jugando = False

    print("")
    if mejor == 0:
        print("You didn't get any round right. Try again!")
    else:
        print("Your best sequence was " + str(mejor) + " digits.")
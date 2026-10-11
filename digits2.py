import random
import time

def jugar():
    total_rondas = 5
    aciertos = 0
    ronda = 0

    print("")
    print("=== LIGHTNING CALCULATOR ===")
    print("Solve 5 problems as fast as you can.")
    print("Your total time is measured, so don't get distracted.")
    print("")
    input("Press Enter to start...")

    inicio = time.time()

    while ronda < total_rondas:
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        op = random.choice(["+", "-", "*"])

        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        else:
            resultado = a * b

        if op == "*":
            simbolo = "x"
        else:
            simbolo = op

        print("")
        print("Question " + str(ronda + 1) + " of " + str(total_rondas))

        pidiendo = True
        while pidiendo:
            try:
                respuesta = int(input(str(a) + " " + simbolo + " " + str(b) + " = "))
                pidiendo = False
            except ValueError:
                print("That is not a whole number, try again.")

        if respuesta == resultado:
            print("Correct!")
            aciertos = aciertos + 1
        else:
            print("Wrong, it was " + str(resultado))

        ronda = ronda + 1

    total = round(time.time() - inicio, 1)

    print("")
    print("You got " + str(aciertos) + " out of " + str(total_rondas))
    print("Total time: " + str(total) + " seconds")

    if aciertos == total_rondas:
        print("Perfect! Calculator brain.")
    elif aciertos >= 3:
        print("Well done!")
    else:
        print("Keep practicing, you can do it!")
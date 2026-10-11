import digits
import digits1
import digits2
import digits3

seguir = True

while seguir:
    print("")
    print("=== DIGITS ===")
    print("1. Adivina el número")
    print("2. Dados de la suerte")
    print("3. Calculadora relámpago")
    print("4. Memoria de dígitos")
    print("0. Salir")

    opcion = input("Elige un juego: ").strip()

    if opcion == "1":
        digits.jugar()
    elif opcion == "2":
        digits1.jugar()
    elif opcion == "3":
        digits2.jugar()
    elif opcion == "4":
        digits3.jugar()
    elif opcion == "0":
        print("¡Gracias por jugar Digits! Hasta pronto.")
        seguir = False
    else:
        print("Esa opción no existe, elige un número del 0 al 4.")
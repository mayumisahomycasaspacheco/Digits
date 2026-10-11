import digits
import digits1
import digits2
import digits3

seguir = True

while seguir:
    print("")
    print("=== DIGITS ===")
    print("1. Guess the Number")
    print("2. Lucky Dice")
    print("3. Lightning Calculator")
    print("4. Digit Memory")
    print("0. Exit")

    opcion = input("Choose a game: ").strip()

    if opcion == "1":
        digits.jugar()
    elif opcion == "2":
        digits1.jugar()
    elif opcion == "3":
        digits2.jugar()
    elif opcion == "4":
        digits3.jugar()
    elif opcion == "0":
        print("Thanks for playing Digits! See you soon.")
        seguir = False
    else:
        print("That option doesn't exist, choose a number from 0 to 4.")
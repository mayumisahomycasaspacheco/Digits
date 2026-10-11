import random

def jugar():
    monedas = 10
    jugando = True

    print("¡Bienvenidos a Dados de la suerte!")
    print("Apuesta monedas y adivina la suma de dos dados:")
    print("Elige una suma baja (2-6), siete o suma alta (8-12) y tira los dados.")
    print("Baja y alta pagan lo apostado. Siete paga el triple.")

    while jugando and monedas > 0:
        print("")
        print("Tienes " + str(monedas) + " monedas")

        pidiendo_apuesta = True
        while pidiendo_apuesta:
            try:
                apuesta = int(input("¿Cuántas monedas quieres apostar? "))
                if apuesta < 1:
                    print("Tienes que apostar al menos 1 moneda.")
                elif apuesta > monedas:
                    print("No puedes apostar más de lo que tienes (" + str(monedas) + ").")
                else:
                    pidiendo_apuesta = False
            except ValueError:
                print("Eso no es un número entero, intenta otra vez.")

        pidiendo_eleccion = True
        while pidiendo_eleccion:
            eleccion = input("Elige baja, siete o alta: ").lower().strip()
            if eleccion == "baja" or eleccion == "siete" or eleccion == "alta":
                pidiendo_eleccion = False
            else:
                print("Opción inválida. Escribe exactamente: baja, siete o alta.")

        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        suma = dado_1 + dado_2
        print("Salió " + str(dado_1) + " y " + str(dado_2) + ": suma " + str(suma))

        if eleccion == "baja" and suma < 7:
            print("¡Ganaste " + str(apuesta) + " monedas!")
            monedas = monedas + apuesta
        elif eleccion == "alta" and suma > 7:
            print("¡Ganaste " + str(apuesta) + " monedas!")
            monedas = monedas + apuesta
        elif eleccion == "siete" and suma == 7:
            print("¡Siete exacto! Ganaste " + str(apuesta * 3) + " monedas")
            monedas = monedas + apuesta * 3
        else:
            print("Perdiste " + str(apuesta) + " monedas")
            monedas = monedas - apuesta

        if monedas > 0:
            pidiendo_seguir = True
            while pidiendo_seguir:
                otra = input("¿Seguir jugando? (s/n): ").lower().strip()
                if otra == "s":
                    pidiendo_seguir = False
                elif otra == "n":
                    pidiendo_seguir = False
                    jugando = False
                else:
                    print("Escribe solo s o n.")

    if monedas <= 0:
        print("Te quedaste sin monedas. ¡Fin del juego!")
    else:
        print("Te retiraste con " + str(monedas) + " monedas.")
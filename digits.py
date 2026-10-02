import random

def jugar():
    numero_secreto_1 = random.randint(1, 50)
    numero_secreto_2 = random.randint(1, 100)
    numero_secreto_3 = random.randint(1, 500)

    maximo_intentos = 10
    contador_intentos = 0
    adivinado = False

    print("Bienvenido a Digits")
    print("Elige una dificultad")
    print("1. Facil (1-50)")
    print("2. Medio (1-100)")
    print("3. Dificil (1-500)")

    opcion = input("Escoge una opcion: ")

    if opcion == "1":
        while not adivinado and contador_intentos < maximo_intentos:
            correcto = True
            while correcto:
                try:
                    intento = int(input("Ingresa un numero: "))
                    correcto = False
                except ValueError:
                    print("Ese no es un numero, intenta otra cosa.")
            contador_intentos = contador_intentos + 1
                
            if intento < numero_secreto_1:
                print("El numero es más alto")
            elif intento > numero_secreto_1:
                print("El numero es más bajo")
            else:
                print("¡Felicidades! Encontraste el numero secreto")
                adivinado = True
        if adivinado:
            print("Lo lograste en: " + str(contador_intentos) + " intentos.")
        else:
            print("Te quedaste sin intentos. El numero era " + str(numero_secreto_1))     

    elif opcion == "2":
        while not adivinado and contador_intentos < maximo_intentos:
            correcto = True
            while correcto:
                try:
                    intento = int(input("Ingresa un numero: "))
                    correcto = False
                except ValueError:
                    print("Ese no es un numero, intenta otra cosa.")
            contador_intentos = contador_intentos + 1
            
            if intento < numero_secreto_2:
                print("El numero es mas alto")
            elif intento > numero_secreto_2:
                print("El numero es mas bajo")
            else:
                print("¡Felicidades! Encontraste el numero secreto")
                adivinado = True
        if adivinado:
            print("Lo lograste en: " + str(contador_intentos) + " intentos.")
        else:
            print("Te quedaste sin intentos. El numero era " + str(numero_secreto_2))          
            

    elif opcion == "3":
        while not adivinado and contador_intentos < maximo_intentos:
            correcto = True
            while correcto:
                try:
                    intento = int(input("Ingresa un numero: "))
                    correcto = False
                except ValueError:
                    print("Ese no es un numero, intenta otra cosa.")
            contador_intentos = contador_intentos + 1
            
            if intento < numero_secreto_3:
                print("El numero es mas alto")
            elif intento > numero_secreto_3:
                print("El numero es mas bajo")
            else:
                print("¡Felicidades! Encontraste el numero secreto")
                adivinado = True
        if adivinado:
            print("Lo lograste en: " + str(contador_intentos) + " intentos.")
        else:
            print("Te quedaste sin intentos. El numero era " + str(numero_secreto_3))
    else:
        print("Esa opcion no existe, prueba con un numero del 1 al 3")

jugar()
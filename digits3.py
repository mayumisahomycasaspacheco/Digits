import random
import time

def jugar():
    largo = 3
    mejor = 0
    jugando = True
    
    print("")
    print("===MEMORIA DE DÍGITOS===")
    print("Verás una secuencia de númSeros por segundos.")
    print("Memorízala y escríbela. Cada ronda tendrá un dígito más.")
    print(" ")
    input("Presiona Enter para empezar...")
    
    while jugando:
        secuencia = ""
        i = 0
        while i < largo:
            secuencia = secuencia + str(random.randint(0, 9))
            i = i + 1
            
            print("")
            print("Memoriza: " + secuencia)
            time.sleep(1 + largo * 0.5)
            print("\n" * 40)
            
            pidiendo = True
            while pidiendo:
                respuesta = input("¿Cuál era la secuencia? ").strip()
                if not respuesta.isdigit():
                    print ("Escribe solo dígitos, sin letras ni espacios.")
                elif len(respuesta) != largo:
                    print("La secuencia tenía " + str(largo) + " dígitos.")
                else:
                    pidiendo = False
                
            if respuesta == secuencia:
                print("¡Correcto!")
                mejor = largo
                largo = largo + 1
            else:
                print("Incorrecto, era " + secuencia)
                jugando = False
            
        print("")
        if mejor == 0:
            print("No lograste ninguna ronsa. ¡Intentalo de nuevo!")
        else:
            print("Tu mejor secuencia fue de " + str(mejor) + "dígitos.")
            
            
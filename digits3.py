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
            
            
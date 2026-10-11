import random
import time

def jugar():
    total_rondas = 5
    aciertos = 0
    ronda = 0
    
    print("")
    print("===CALCULADORA RELÁMPAGO===")
    print("Resuelve 5 ejercicios lo más rápido que puedas.")
    print("Se mide el tiempo total, asi que no te distraigas.")
    print("")
    input("Presiona enter para comenzar...")
    
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
        
        pidiendo = True
        while pidiendo:
            try:
                texto = str(ronda + 1) + "/" + str(total_rondas) + " " + str(a) + " " + op + " " + str(b) + " = "
                respuesta = int(input(texto))
                pidiendo = False
            except ValueError:
                print("Eso no es un número entero, intenta otra vez.")
                
        if respuesta == resultado:
            print("¡Correcto!")
            aciertos = aciertos + 1
        else:
            print("Incorrecto, era " + str(resultado))
        
        ronda = ronda + 1
        
    total = round(time.time() - inicio, 1)
    
    print("")
    print("Acertaste" + str(aciertos) + " de " + str(total_rondas))
    print("Tiempo total: " + str(total) + " segundos")
    
    if aciertos == total_rondas:
        print("¡Perfecto!. Cerebro de calculadora.")
    elif aciertos >= 3:
        print("¡Bien hecho!")
    else:
        print("Sigue practicando, ¡Tú puedes!")
        
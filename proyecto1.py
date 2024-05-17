import time

def numero_que_adivinado():
    
    # Panel de inicio del juego en secuencia
    print("======================================")
    time.sleep(1)
    print("          !!!bienvenido!!!            ")
    time.sleep(1)
    print("======================================")
    time.sleep(1)
    print("======¿dime un numero entero?=========")
    time.sleep(1)
    print("=====y te dire si es par o impar======")
    time.sleep(1)
    
    # pide al usuario un numero entero

    numero_que_adivino = int(input("¿que numero estas pensando?:"))

    if numero_que_adivino % 2 == 0:
        print("El numero que pensaste es Par")

    else:
        print("El numero que pensaste es Impar")

numero_que_adivinado()

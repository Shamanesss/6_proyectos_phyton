# importamos un modulo ramdom para usar un proceso aleatorio
import random


def get_number(num):

    print("Vamos a jugar adivinar un numero")
    print("¿Estas preparado?")
    print("Pues empecemos")

    # usamos random para aleatorio y randint para usar un numero entero aleatorio usa dos parametros para usar un rango
    # numero entre 1 y el numero introducido
    numero_aleatorio = random.randint(1, num)
    numero_adivinar = 0

    while numero_adivinar != numero_aleatorio:
        # el usuario ingresa un numero
        numero_adivinar = int(input(f"Adivina un numero entre 1 y {num}: "))

        if numero_adivinar < numero_aleatorio:
            print("El numero es mas alto")
        elif numero_adivinar > numero_aleatorio:
            print("El numero es mas bajo")

    print(f"!Feliciadades¡ el numero es {numero_aleatorio}")


get_number(10)

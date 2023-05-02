# la computadora tiene que adivinar nuestro numero
import random


def adivina_mi_numero(num):

    print("Juego de adivinar mi numero")

    print(
        f"Selecciona un numero entre 1 y {num} para que la computadora lo adivine")
    # rango de numeros
    numero_inferior = 1
    numero_superior = num

    solucion = ""
    while solucion != "c":
        # prediccion
        if numero_inferior != numero_superior:
            predecir = random.randint(numero_inferior, numero_superior)
        else:
            predecir = numero_inferior

        # obtener respuesta del usuario
        solucion = input(
            f"El numero creo que es {predecir}\n Si es menor, ingresa A \n Si es mayor, ingresa B \n Si es correcto, ingresa C \n").lower()

        if solucion == "a":
            numero_superior = predecir - 1
        elif solucion == "b":
            numero_inferior = predecir + 1
    print(f"El numero es {predecir}")


adivina_mi_numero(20)

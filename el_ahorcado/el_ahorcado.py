# tienes sieta vidas para adivinar la palabar

import string
import random

from palabras import palabras
from ahorcado_dibujo import vidas_diccionario_visual


def obtener_palabra(palabra):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():
    palabra = obtener_palabra(palabras)

    letras_preguntar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)  # esto no contiene la ñ

    # el numero de vidas es de 7
    vidas = 7

    while len(letras_preguntar) > 0 and vidas > 0:
        print(
            f"Te quedan {vidas} vidas \n Has usado estas letras: {' '.join(letras_adivinadas)}")

        # mostrar el estado  actual de la palabra
        solucion_lista = [
            letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(solucion_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # si la letra escogido  por el usuario esta en el abecedario y no esta en el conjunto
        # de letras que ya se ha ingresado, se añade la letra al conjunto de letras ingresadas

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # preguntamos si esta en la palabra quitar la letra del conjunto de letras pendiente por adivinar
            # si no esta quitar un vida
            if letra_usuario in letras_preguntar:
                letras_preguntar.remove(letra_usuario)
                print(' ')
            else:
                vidas = vidas - 1
                print(f"\n Tu letra, {letra_usuario} no esta en la palabra")

        # si la letra escogida por el usuario ya fu ingresada

        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogiste esa letra. Escoge una nueva")
        else:
            print("Esta letra no es valida")
    # Cuando se adivina todas las letras de la palabra o pierde todas la vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. La palabras era: {palabra}")
    else:
        print(f"Excelente la palabra era {palabra}")


ahorcado()

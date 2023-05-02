# tenemos dos usuarios
# uno la computadora y otro el usuario
import random


def jugar():
    usuario = input(
        "Escoge una opcion: \n Piedra - pulsa Piedra  \n Papel - pulsa papel \n Tijeras - pulsa Tijera \n").lower()
    computadora = random.choice(['piedra', 'papel', 'tijera'])

    if usuario == computadora:
        print(f"Has elegido {usuario} y yo {computadora}")
        return '¡Empate!'

    if has_ganado(usuario, computadora):
        print(f"Has elegido {usuario} y yo {computadora}")
        return '¡Ganaste!'

    print(f"Has elegido {usuario} y yo {computadora}")
    return '¡Perdiste!'


def has_ganado(jugador, oponente):
    if ((jugador == 'p' and oponente == 't') or (jugador == 't' and oponente == 'w') or (jugador == 'w' and oponente == 'p')):
        return True
    else:
        return False


print(jugar())

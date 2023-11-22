

# Juego del Ahorcado
# ----------------------------------------------------------------------------------------------------------------------

# 1. Librerías
from random import choice


# 2. Funciones
def palabra_aleatoria() -> str:
    """
    Dado un listado de palabras dentro de la función, escoge una de forma aleatoria.
    :return: Palabra.
    """
    palabras = [
        "manzana", "plátano", "uva", "fresa", "kiwi", "piña", "mango", "pera", "cereza", "sandía",
        "melón", "naranja", "limón", "frambuesa", "mandarina", "papaya", "granada", "ciruela", "coco", "guayaba"
    ]
    return choice(palabras)


def pedir_letra() -> str:
    """
    Solicita una letra al usuario, y comprueba si se encuentra en el abecedario. En caso contrario, solicita un nuevo
    caracter hasta que cumpla la condición mencionada.
    :return: Devuelve la letra validada introducidad por el usuario.
    """
    letra_usuario = ''
    letra_valida = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while letra_valida is False:
        letra_usuario = input("Introduce una letra: ").lower()
        if letra_usuario in abecedario and len(letra_usuario) == 1:
            letra_valida = True
        else:
            print(f"Error, {letra_usuario} no es un caracter válido.")

    return letra_usuario


def pintar_palabra(palabra: str, letras_correctas: list) -> str:
    """
    Dada una palabra a adivinar, y una lista de letras correctas, comprueba letra a letra de la palabra si se encuentra
    en la lista de letras correctas, y en caso afirmativo pinta la letra, en caso negativo pinta un guión.
    :param palabra: Palabra a adivinar.
    :param letras_correctas: Listado de letras que ha ido acertando el juego.
    :return: Palabra formada por guiones, con los guiones sustituidos por las letras que se han ido acertando.
    """
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado = resultado + letra
        else:
            resultado = resultado + "_"

    return resultado


def jugar_ahorcado():
    # Variables del juego
    vidas = 6
    intentos_realizados = 0
    palabra_a_adivinar = palabra_aleatoria()
    letras_correctas = []
    letras_incorrectas = []

    print("¡Bienvenido al juego del ahorcado!")
    print("¡La palabra a adivinar tiene la siguiente longitud: ")
    print(pintar_palabra(palabra_a_adivinar, letras_correctas))
    print("")

    while True:

        letra_ingresada = pedir_letra()

        if letra_ingresada in letras_correctas:
            print("Ya has intentado esa letra. Intenta con otra.")
        elif letra_ingresada in letras_incorrectas:
            print("Ya has intentado esa letra. Intenta con otra.")
        elif letra_ingresada in palabra_a_adivinar:
            letras_correctas.append(letra_ingresada)
            print("Bien hecho, letra correcta!")
        else:
            letras_incorrectas.append(letra_ingresada)
            intentos_realizados = intentos_realizados + 1

        print(f"Palabra: {pintar_palabra(palabra_a_adivinar, letras_correctas)}")
        print(f"Intentos restantes: {vidas - intentos_realizados}")

        if set(letras_correctas) == set(palabra_a_adivinar):
            print("¡Felicidades! Has adivinado la palabra.")
            break
        elif intentos_realizados == vidas:
            print(f"¡Oh no! Has agotado tus intentos. La palabra era '{palabra_a_adivinar}'.")
            break
        else:
            continue


# 3. Inicializar juego
if __name__ == "__main__":
    jugar_ahorcado()

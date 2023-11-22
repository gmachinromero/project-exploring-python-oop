from random import randint


def sumar(num1: int, num2: int) -> int:
    """
    Devuelve la suma de dos números enteros.
    :param num1: número entero
    :param num2: número entero
    :return: número entero
    """
    return num1+num2


def lanzar_dados() -> tuple:
    """
    Simula la tirada de dos dados.
    :return: Devuelve una tupla formada por 2 int, con el valor de cada tirada.
    """
    dado_1 = randint(1, 6)
    dado_2 = randint(1, 6)
    return dado_1, dado_2


def evaluar_jugada(dado_1: int, dado_2: int) -> None:
    """
    Dada la tirada de dos dados, evalua si es una buena jugada o no.
    :param dado_1: Tirada del dado 1
    :param dado_2: Tirada del dado 2
    :return: None
    """

    suma_dados = dado_1 + dado_2

    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


dado_1, dado_2 = lanzar_dados()
evaluar_jugada(dado_1, dado_2)



def suma(*args):
    return sum(args)

print(suma(1, 2, 10, 4))


def suma_cuadrados(*args):
    total = 0
    for i in args:
        total += i**2
    return total

print(suma_cuadrados(1,2,3))


def numeros_persona(nombre, *args):
    print(f"{nombre}, la suma de tus números es {sum(args)}")

numeros_persona("Federico", 75,20,65)



def cantidad_atributos(**kwargs):
    print(len(kwargs))

cantidad_atributos(x=1, y=2, z=3)


def lista_atributos(**kwargs):
    print(list(kwargs.values()))

lista_atributos(x=1, y=2, z=3)



def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for i, j in kwargs.items():
        print(f"{i}: {j}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")


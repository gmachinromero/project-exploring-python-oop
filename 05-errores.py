
def suma():
    num1 = int(input("Introduce número 1: "))
    num2 = int(input("Introduce número 1: "))
    print(num1 + num2)
    print("Gracias por usar el programa suma :)")


try:
    # Código que queremos probar
    suma()
except:
    # Código a ejecutar si hay un error
    print("Algo no ha salido bien.")
else:
    # Código a ejecutar adicional si no hubo fallo en try
    print("Todo ha ido bien.")
finally:
    # Código que se va a ejecutar de todas formas
    print("Esto es todo amigos.")


def suma2():
    num1 = int(input("Introduce número 1: "))
    num2 = int(input("Introduce número 1: "))
    print(num1 + num2)
    print("Quieres sumar los numéros " + num1 + " y " + num2)


try:
    # Código que queremos probar
    suma2()
except TypeError:
    # Código a ejecutar si hay un error
    print("Estás intentando concatenar tipos distintos de datos")
except ValueError:
    # Código a ejecutar si hay un error
    print("Eso no es un número")
else:
    # Código a ejecutar adicional si no hubo fallo en try
    print("Todo ha ido bien.")
finally:
    # Código que se va a ejecutar de todas formas
    print("Esto es todo amigos.")

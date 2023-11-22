

# Recetario
# ----------------------------------------------------------------------------------------------------------------------

# 1. Librerías
import os
from pathlib import Path


# 2. Funciones
def listar_ruta(ruta):
    # Definir el directorio base
    directorio_base = Path(ruta)
    # Utilizar el método rglob para buscar archivos recursivamente
    archivos_txt = directorio_base.rglob("*.txt")
    # Imprimir la lista de archivos encontrados
    contador = 0
    for archivo in archivos_txt:
        contador = contador + 1
        print("- " + archivo.stem)

    print(f"El recetario contiene {contador} recetas.")


def opciones_usuario():
    print("Las opciones disponible son: ")
    print("[1]: Mostar una receta")
    print("[2]: Crear una receta")
    print("[3]: Crear una categoría")
    print("[4]: Eliminar una receta")
    print("[5]: Eliminar una categoría")
    print("[6]: Finalizar ejecución")
    print("")

    opcion_usuario = 0

    while opcion_usuario not in range(1, 7):
        opcion_usuario = int(input("¿Qué acción quiere realizar?: "))
        if opcion_usuario not in range(1, 7):
            print("Valor no válido, introduzca una opción del 1 al 6.")
        else:
            pass

    return opcion_usuario


def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador = contador + 1

    return lista_categorias


def elegir_categorias(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista)+1):
        eleccion_correcta = input("Elije una categoría: ")

    return lista[int(eleccion_correcta)-1]


def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador = contador + 1

    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input("Elije una receta: ")

    return lista[int(eleccion_receta)-1]


def leer_recetas(receta):
    print(Path.read_text(receta))


def crear_recetas(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print(f"Lo siento, esa receta ya existe.")


def crear_categorias(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print(f"Lo siento, esa categoria ya existe.")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido elimianda")


def iniciar_recetario():
    # Variables del recetario:
    ruta_recetario = "/home/gmachin/git/personal/project-exploring-python-oop/files/Recetas"

    # Listar recetas:
    print(f"Bienvenido al recetario de la Guilla!!")
    print(f"La ruta donde se encuentran las recetas es: {ruta_recetario}")
    listar_ruta(ruta_recetario)
    print("")

    # Comienzo del bucle
    while True:

        # Consultar al usuario
        opcion_usuario = opciones_usuario()

        # Flujo
        if opcion_usuario == 1:
            # mostrar categorías
            mis_categorias = mostrar_categorias(ruta_recetario)
            # elegir categoría
            mi_categoria = elegir_categorias(mis_categorias)
            # mostrar recetas
            mis_recetas = mostrar_recetas(mi_categoria)
            # elegir recetas
            mi_receta = elegir_recetas(mis_recetas)
            # leer receta
            leer_recetas(mi_receta)

        elif opcion_usuario == 2:
            # mostrar categorías
            mis_categorias = mostrar_categorias(ruta_recetario)
            # elegir categoría
            mi_categoria = elegir_categorias(mis_categorias)
            # crear receta nueva
            crear_recetas(mi_categoria)

        elif opcion_usuario == 3:
            # crear categorías
            crear_categorias(ruta_recetario)

        elif opcion_usuario == 4:
            # mostrar categorías
            mis_categorias = mostrar_categorias(ruta_recetario)
            # elegir categoría
            mi_categoria = elegir_categorias(mis_categorias)
            # mostrar recetas
            mis_recetas = mostrar_recetas(mi_categoria)
            # elegir recetas
            mi_receta = elegir_recetas(mis_recetas)
            # eliminar receta
            eliminar_receta(mi_receta)

        elif opcion_usuario == 5:
            # mostrar categorías
            mis_categorias = mostrar_categorias(ruta_recetario)
            # elegir categoría
            mi_categoria = elegir_categorias(mis_categorias)
            # eliminar categoría
            eliminar_categoria(mi_categoria)

        else:
            print("Ejecución finalizada.")
            break






# 3. Inicializar recetario
if __name__ == "__main__":
    iniciar_recetario()

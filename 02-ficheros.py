
# Librerías
import os
from pathlib import Path


# Abrir un archivo, leer, cerrar
mi_archivo = open("files/prueba_lectura.txt")
print(mi_archivo)
mi_archivo.close()


# Abrir un fichero en modo lectura
with open("files/prueba_lectura.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# Abrir un fichero en modo escritura overwrite. Si no existe lo crea.
with open("files/prueba_escritura.txt", "w") as archivo:
    # Escritura multilinea
    archivo.write("""
    Esto es una prueba de escritura multilínea:
    - Línea 1
    - Línea 2
    - Línea 3
    - ...
    """)
    # Escritura por lista
    archivo.write("\n")
    archivo.write(50*"*")
    archivo.write("\n")
    archivo.writelines(["otra ", "prueba ", "de ", "escritura"])


# Abrir un fichero en modo escritura append
with open("files/prueba_escritura.txt", "a") as archivo:
    archivo.write("\n")
    archivo.write(50*"*")
    archivo.write("\n")
    archivo.write("Escribiendo en modo Append desde el último caracter.")


# Abrir fichero con la clase Path para asegurar compatbilidad entre OS
carpeta = Path("//files")
archivo = carpeta / "prueba_lectura.txt"
with open(archivo) as mi_archivo:
    print(mi_archivo.read())


# Prueba con directorios
ruta = os.getcwd()
print(ruta)

# Obtener el basename y dirname de una ruta
ruta = "/home/gmachin/git/personal/project-exploring-python-oop/prueba_escritura.txt"
fichero = os.path.basename(ruta)
directorio = os.path.dirname(ruta)
print(fichero)
print(directorio)

# Crar directorio y eliminar
print(os.getcwd())
os.makedirs("carpeta_nueva")
os.rmdir("carpeta_nueva")


from pathlib import Path, PureWindowsPath

# Leer fichero, sin abrirlo
mi_archivo = Path("//files/prueba_lectura.txt")
print(type(mi_archivo))
print(mi_archivo.read_text())

# Leer fichero, sin abrirlo
mi_archivo = Path("//files/prueba_lectura.txt")
print(type(mi_archivo))
print(mi_archivo.name)
print(mi_archivo.suffix)
print(mi_archivo.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Sí existe")

mi_archivo = Path("//files/prueba_lectura.txt")
mi_archivo_windows = PureWindowsPath(mi_archivo)
print(mi_archivo_windows)


# Programación orientada a objetos:
# ----------------------------------------------------------------------------------------------------------------------

# Crear una clase
class Pajaro:
    pass


mi_pajaro_1 = Pajaro()
mi_pajaro_2 = Pajaro()

print(type(mi_pajaro_1))

print(mi_pajaro_1)
print(mi_pajaro_2)


# Crear una clase con atributos (de clase y de instancia)
class Pajaro:
    # Atributo de clase
    alas = True

    # Atributo de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro_1 = Pajaro("verde", "tucan")
print(mi_pajaro_1.color)
print(mi_pajaro_1.especie)
print(mi_pajaro_1.alas)
print(f"Mi pájaro es un {mi_pajaro_1.especie} de color {mi_pajaro_1.color}")


# Crear una clase con atributos y métodos de instancia
class Mago:
    # Atributo de clase
    es_mago = True
    hogwarts = True

    # Atributo de instancia
    def __init__(self, nombre, casa, varita, hechizo_favorito):
        self.nombre = nombre
        self.casa = casa
        self.varita = varita
        self.hechizo_favorito = hechizo_favorito

    # Métodos
    def lanzar_hechizo_fav(self):
        print(f"{self.nombre} ha lanzado {self.hechizo_favorito} con su varita de {self.varita}")

    def ganar_puntos(self, puntos):
        print(f"{self.nombre} ha ganado {puntos} puntos para la casa {self.casa}")


harry_potter = Mago(
    "Harry Potter",
    "Gryffindor",
    "Sauco",
    "Sectusempra!"
)

draco_malfoy = Mago(
    "Draco Malfoy",
    "Slythering",
    "Ebano",
    "Eres una Sangre Sucia!"
)

harry_potter.lanzar_hechizo_fav()
harry_potter.ganar_puntos(50)

draco_malfoy.lanzar_hechizo_fav()
draco_malfoy.ganar_puntos(-20)


# Clase con métodos de instancia, de clase y estáticos
class Mago:
    # Atributo de clase
    es_mago = True
    in_hogwarts = True

    # Atributo de instancia
    def __init__(self, nombre, casa, varita, hechizo_favorito):
        self.nombre = nombre
        self.casa = casa
        self.varita = varita
        self.hechizo_favorito = hechizo_favorito

    # Métodos de instancia, cambian atributos de instancia y de clase
    def lanzar_hechizo_fav(self):
        print(f"{self.nombre} ha lanzado {self.hechizo_favorito} con su varita de {self.varita}")

    def ganar_puntos(self, puntos):
        print(f"{self.nombre} ha ganado {puntos} puntos para la casa {self.casa}")

    def expulsado_hogwarts(self):
        self.in_hogwarts = False
        print(f"{self.nombre} ha sido expulsado de hogwarts")

    def admitido_hogwarts(self):
        self.in_hogwarts = True
        print(f"{self.nombre} ha sido admitido en hogwarts")

    # Métodos de clase, pueden acceder y modificar atributos de clase, pero no de instancia
    @classmethod
    def mago_verificado(cls):
        cls.es_mago = True
        print(f"Es un mago")

    # Métodos estáticos, no tiene acceso a los atributos de la instancia ni de la clase
    @staticmethod
    def abrir_puerta():
        print(f"Alohomora!")


harry_potter = Mago(
    "Harry Potter",
    "Gryffindor",
    "Sauco",
    "Sectusempra!"
)

print(harry_potter.in_hogwarts)
harry_potter.expulsado_hogwarts()
print(harry_potter.in_hogwarts)

harry_potter.mago_verificado()
Mago.mago_verificado()

harry_potter.abrir_puerta()
Mago.abrir_puerta()


# Herencia
class Persona:
    # Atributo de instancia
    def __init__(self, edad, genero, altura):
        self.edad = edad
        self.genero = genero
        self.altura = altura

    def nacer(self):
        print("Esta persona ha nacido")


class Mago(Persona):
    # Atributo de instancia
    def __init__(self, edad, genero, altura, nombre, casa, varita, hechizo_favorito):
        super().__init__(edad, genero, altura)
        self.nombre = nombre
        self.casa = casa
        self.varita = varita
        self.hechizo_favorito = hechizo_favorito

    def nacer(self):
        print("Este mago ha nacido")


# Clase origen de Mago
print(Mago.__bases__)

# Subclases de la (super)clase Persona
print(Persona.__subclasses__())

# Orden de prioridad de las clases que forman la clase Mago
print(Mago.__mro__)

harry_potter = Mago(
    21,
    "Masculino",
    172,
    "Harry Potter",
    "Gryffindor",
    "Sauco",
    "Sectusempra"
)

harry_potter.nacer()


# Polimorfismo
class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice muuuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice beeee")


vaca_1 = Vaca('Aurora')
oveja_1 = Oveja('Maya')

rebanio = [vaca_1, oveja_1]

for animal in rebanio:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca_1)
animal_habla(oveja_1)


# Ejercicios
"""
Ejercicio 1
- Crea una clase llamada Punto con sus dos coordenadas X e Y.
- Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
- Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y).
- Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto.
- Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
- Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla.
"""


class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante 1."
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2."
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3."
        elif self.x > 0 and self.y < 0:
            return "Cuadrante 4."
        elif self.x == 0 and self.y == 0:
            return "Origen de coordenas."
        elif self.x == 0 and self.y != 0:
            return "Eje X."
        elif self.x != 0 and self.y == 0:
            return "Eje Y."
        else:
            return "Error."

    def vector(self, punto):
        componente_x = punto.x - self.x
        componente_y = punto.y - self.y
        return f"({componente_x}, {componente_y})"


punto_1 = Punto(2, 3)
punto_2 = Punto(-2, 3)
punto_3 = Punto(-2, -3)
punto_4 = Punto(2, -3)
punto_origen = Punto()

print(punto_1.cuadrante())
print(punto_2.cuadrante())
print(punto_3.cuadrante())
print(punto_4.cuadrante())
print(punto_origen.cuadrante())

print(punto_1.vector(punto_2))
print(punto_1.vector(punto_3))

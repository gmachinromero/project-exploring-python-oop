
import unittest

# Clase a ser testeada
class Rectangulo:
    
    def __init__(self, anchura, altura):
        self.anchura = anchura
        self.altura = altura

    def calcular_area(self):
        return self.anchura * self.altura

    def calcular_perimetro(self):
        return 2*self.anchura + 2*self.altura

    def modificar_anchura(self, anchura):
        self.anchura = anchura

    def modificar_altura(self, altura):
        self.altura = altura
        

# Test unitarios
class TestCalculoArea(unittest.TestCase):
    
    def test_calcular_area(self):
        rectangulo = Rectangulo(2, 3)
        test = rectangulo.calcular_area()
        test_ok = 6
        self.assertEqual(test, test_ok, "Error: Area incorrecta.")

    def test_calcular_perimetro(self):
        rectangulo = Rectangulo(2, 3)
        test = rectangulo.calcular_perimetro()
        test_ok = 10
        self.assertEqual(test, test_ok, "Error: Perímetro incorrecto.")


class TestRectangulo(unittest.TestCase):

    def setUp(self):
        self.rectangulo = Rectangulo(0, 0)

    def test_modificar_anchura(self):
        self.rectangulo.modificar_anchura(8)
        self.assertEqual(self.rectangulo.anchura, 8)

    def test_modificar_altura(self):
        self.rectangulo.modificar_altura(15)
        self.assertEqual(self.rectangulo.altura, 15)

    def test_modificar_anchura_y_altura(self):
        self.rectangulo.modificar_anchura(8)
        self.rectangulo.modificar_altura(15)
        self.assertEqual(self.rectangulo.anchura, 8)
        self.assertEqual(self.rectangulo.altura, 15)
        self.assertEqual(self.rectangulo.calcular_area(), 120)
        self.assertEqual(self.rectangulo.calcular_perimetro(), 46)


# Ejecutar Test
unittest.main()

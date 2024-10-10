import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_adicionar(self):
        self.assertEqual(self.calc.adicionar(1, 1), 2)
        self.assertEqual(self.calc.adicionar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(1, 1), 0)
        self.assertEqual(self.calc.subtrair(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-1, 5), -5)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertRaises(ValueError, self.calc.dividir, 10, 0)

if __name__ == "__main__":
    unittest.main()

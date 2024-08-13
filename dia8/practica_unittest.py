"""
Probar nuestro código con unittest
"""

import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buenos días"
        resultado = cambia_texto.todo_mayusculas(palabra)

        self.assertEqual("BUENOS DÍAS", resultado)


if __name__ == "__main__":
    unittest.main()

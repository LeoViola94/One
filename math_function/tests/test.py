import unittest
from math_function.math_function.exponential import FunzioneEsponenziale


class TestFunzioneEsponenziale(unittest.TestCase):
    def test_calcola(self):

        funzione = FunzioneEsponenziale(2)


        self.assertEqual(funzione.calcola(0), 1)  # 2^0 = 1
        self.assertEqual(funzione.calcola(1), 2)  # 2^1 = 2
        self.assertEqual(funzione.calcola(2), 4)  # 2^2 = 4
        self.assertEqual(funzione.calcola(3), 8)  # 2^3 = 8


if __name__ == "__main__":
    unittest.main()
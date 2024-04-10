import unittest
from math_function.math_function.exponential import FunzioneEsponenziale


class TestFunzioneEsponenziale(unittest.TestCase):
    def test_calcola(self):
        # Creiamo un'istanza della classe FunzioneEsponenziale con base 2
        funzione = FunzioneEsponenziale(2)

        # Verifichiamo che calcola(2) restituisca 4 (2^2 = 4)
        self.assertEqual(funzione.calcola(2), 4)


if __name__ == "__main__":
    unittest.main()
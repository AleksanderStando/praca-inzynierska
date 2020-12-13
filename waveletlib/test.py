from transform import Transform
from Daubechies import Daubechies
import unittest
import os
from scipy.io import wavfile
from dataTooShortException import DataTooShortException

class TestWavelet(unittest.TestCase):
    def test_correct_size(self):
        wave = Transform(Daubechies(1))
        signal = [1] * 1024
        coeffs = wave.decompose(signal, 10)
        self.assertEqual(len(coeffs[0]), 1)
        self.assertEqual(len(coeffs[1]), 1)
        self.assertEqual(len(coeffs[2]), 2)
        self.assertEqual(len(coeffs[10]), 512)
    def test_incorrect_size(self):
        wave = Transform(Daubechies(3))
        signal = [1] * 1023
        with self.assertRaises(DataTooShortException) as context:
             wave.decompose(signal, 10)


if __name__ == '__main__':
    unittest.main()

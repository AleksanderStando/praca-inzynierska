import sys
import serialization
sys.path.insert(0, '../waveletlib')
from transform import Transform
from Daubechies import Daubechies
import unittest
import os
from scipy.io import wavfile

class TestSerialization(unittest.TestCase):
    def test_serialization(self, path = "Common-Loon-WAV", save_folder = "Common-Loon-Serialized"):
        wave = Transform(Daubechies(3))
        for filename in os.listdir(path):
            samplerate, data = wavfile.read(os.path.join(path, filename))
            time = len(data)/samplerate
            coeffs = wave.decompose(data, 10)
            serialization.serialize(save_folder, coeffs, time, filename, wave.wavelet.family_name, wave.wavelet.dec_len)
            coeffs2, time2, name2 = serialization.deserialize(save_folder, filename)
            self.assertEqual(coeffs2, coeffs)

if __name__ == '__main__':
    unittest.main()

import sys
from scipy.io import wavfile
import os
import level_var


sys.path.insert(0, '../waveletlib')
from transform import Transform
from Daubechies import Daubechies


wave = Transform(Daubechies(3))

level_5_char = level_var.LevelVar(1, 4, 0, 3000, 300)

def test_characteristic(path, char):
    for filename in os.listdir(path):
        samplerate, data = wavfile.read(path + "/" + filename)
        coeffs = wave.decompose(data, 10)
        score = char.calculate(coeffs, 10000)
        print(path + " " + filename + " " + str(score))

test_characteristic(os.path.join("Cut_Data", "Common-Loon-WAV"), level_5_char)
test_characteristic(os.path.join("Cut_Data", "Eurasian-Skylark-WAV"), level_5_char)
test_characteristic(os.path.join("Cut_Data", "House-Sparrow-WAV"), level_5_char)

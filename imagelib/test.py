import generate
import sys
from scipy.io import wavfile
import os

curr = os.getcwd()
print(curr)

sys.path.insert(0, '../waveletlib')
from transform import Transform
from Daubechies import Daubechies


x = [1,2,3,4,3,6,2,8,1,2,3,4,3] * 40

wave = Transform(Daubechies(3))
# coeffs = wave.decompose(x, 6)
#
# plt = generate.generateImage(coeffs, 1000, 1000, "test1")
# generate.saveImage(plt, "test1")

# samplerate, data = wavfile.read('61300')
# coeffs = wave.decompose(data, 20)
# plt = generate.generateImage(coeffs, 1000, 1000, "test2")
# generate.saveImage(plt, "test2")


#samplerate, data = wavfile.read('231048')
#coeffs = wave.decompose(data, 20)
#generate.generateImage(coeffs, 1000, 1000, "test3")

def create_images(path, save_folder_name):
    for filename in os.listdir(path):
        samplerate, data = wavfile.read(os.path.join(path, filename))
        print(filename)
        coeffs = wave.decompose(data, 15)
        print("Generating file...")
        plt = generate.generateImage(coeffs, 1000, 1000, filename)
        save_path = os.path.join("Images", "Daubechies3", save_folder_name, filename)
        generate.saveImage(plt, save_path)


create_images(os.path.join("Cut_Data", "Eurasian-Skylark-WAV") "Eurasian-Skylark")
create_images(os.path.join("Cut_Data", "House-Sparrow-WAV"), "House-Sparrow")

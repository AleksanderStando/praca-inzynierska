import generate
import sys
from scipy.io import wavfile
import os

curr = os.getcwd()

sys.path.insert(0, '../waveletlib')
sys.path.insert(0, '../serializelib')

from transform import Transform
from Daubechies import Daubechies
from serialization import deserialize


x = [1,2,3,4,3,6,2,8,1,2,3,4,3] * 40

wave = Transform(Daubechies(3))
#coeffs = wave.decompose(x, 6)
#
#plt = generate.generateImage(coeffs, 1000, 1000, "test1")
#generate.saveImage(plt, "test1")

samplerate, data = wavfile.read('CL_72717')
coeffs = wave.decompose(data, 10, "PERIODIC")
plt = generate.generateImage(coeffs, 1000, 1000, "test2", log_scale=False, time=10)
generate.saveImage(plt, "common_loon_daub3")
plt = generate.generateImage(coeffs, 1000, 1000, "test2", log_scale=True, time=10)
generate.saveImage(plt, "common_loon_log_daub3")

#samplerate, data = wavfile.read('231048')
#coeffs = wave.decompose(data, 20)
#generate.generateImage(coeffs, 1000, 1000, "test3")

def create_images(path, save_folder_name):
    for filename in os.listdir(path):
        #samplerate, data = wavfile.read(os.path.join(path, filename))
        print(filename)
        coeffs, time, name, family, order = deserialize(path, filename)
        print("Generating file...")
        plt = generate.generateImage(coeffs, 1000, 1000, filename, time = time)
        filename, file_ext = os.path.splitext(filename)
        save_path = os.path.join(save_folder_name, filename)
        generate.saveImage(plt, save_path)

#create_images(os.path.join("szumy-serialized", "mycie_zebow"), "Images/Daubechies3/mycie_zebow")
#create_images(os.path.join("szumy-serialized", "wiatr"), "Images/Daubechies3/wiatr")
#create_images(os.path.join("szumy-serialized", "ocean"), "Images/Daubechies3/ocean")

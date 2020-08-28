import generate
import sys
from scipy.io import wavfile

sys.path.insert(0, '../waveletlib')
import transform
import Daubechies


x = [1,2,3,4,3,6,2,8,1,2,3,4,3] * 40

wave = transform.Transform(Daubechies.Daubechies(3))
coeffs = wave.decompose(x, 6)

plt = generate.generateImage(coeffs, 1000, 1000, "test1")
generate.saveImage(plt, "test1")

samplerate, data = wavfile.read('61300')
coeffs = wave.decompose(data, 20)
plt = generate.generateImage(coeffs, 1000, 1000, "test2")
generate.saveImage(plt, "test2")


#samplerate, data = wavfile.read('231048')
#coeffs = wave.decompose(data, 20)
#generate.generateImage(coeffs, 1000, 1000, "test3")

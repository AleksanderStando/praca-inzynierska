from transform import Transform
import wavelet
from Daubechies import Daubechies
from Symlet import Symlet
from Coiflet import Coiflet
from draw_wavelet import *

import pywt

x = [1,2,3,4,5,6,7,8, 9] * 3

print("waveletlib:")
wave = Transform(Daubechies(2))
print(wave.decompose(x, 2))

print("pywt library:")

coeffs = pywt.wavedec(x, 'db2', level=2, mode='symmetric')
print(coeffs)

print("***")

print("waveletlib:")
wave = Transform(Symlet(2))
print(wave.decompose(x, 2))

print("pywt library:")

coeffs = pywt.wavedec(x, 'sym2', level=2, mode='symmetric')
print(coeffs)

print("***")

print("waveletlib:")
wave = Transform(Coiflet(1))
print(wave.decompose(x, 2))

print("pywt library:")

coeffs = pywt.wavedec(x, 'coif1', level=2, mode='symmetric')
print(coeffs)

draw_wavelet(Daubechies(2))

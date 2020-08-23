import transform
import wavelet
import Daubechies
import Symlet
import Coiflet

import pywt

x = [1,2,3,4,5,6,7,8, 9] * 3

wave = transform.Transform(Daubechies.Daubechies(2))
print(wave.decompose(x, 1))

print("pywt library:")

coeffs = pywt.wavedec(x, 'db2', level=1, mode='symmetric')
print(coeffs)

print("***")

wave = transform.Transform(Symlet.Symlet(2))
print(wave.decompose(x, 1))

print("pywt library:")

coeffs = pywt.wavedec(x, 'sym2', level=1, mode='symmetric')
print(coeffs)

print("***")

wave = transform.Transform(Coiflet.Coiflet(1))
print(wave.decompose(x, 1))

print("pywt library:")

coeffs = pywt.wavedec(x, 'coif1', level=1, mode='symmetric')
print(coeffs)

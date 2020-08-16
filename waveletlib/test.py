import transform
import fastWaveletTransform
import wavelet
import Daubechies2

import pywt

x = [1,2,3,4,5,6,7,8, 9]

wave = transform.Transform(Daubechies2.Daubechies2(1))
print(wave.decompose(x, 1))

print("pywt library:")

coeffs = pywt.wavedec(x, 'db1', level=1, mode='symmetric')
print(coeffs)

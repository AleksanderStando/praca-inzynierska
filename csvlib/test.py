import save_as_csv
import sys
from scipy.io import wavfile

sys.path.insert(0, '../waveletlib')
import transform
import Daubechies


x = [1,2,3,4,3,6,2,8,1,2,3,4,3] * 40

wave = transform.Transform(Daubechies.Daubechies(1))
coeffs = wave.decompose(x, 6)

save_as_csv.save_transform(coeffs, "test1")

samplerate, data = wavfile.read('61300')
coeffs = wave.decompose(data, 20)
save_as_csv.save_transform(coeffs, "test2")

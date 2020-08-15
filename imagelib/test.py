import generate
import sys

sys.path.insert(0, '../waveletLib')
import transform
import Daubechies2


x = [1,2,3,4,3,6,2,8,1,2,3,4,3] * 40

wave = transform.Transform(Daubechies2.Daubechies2(1))
coeffs = wave.decompose(x, 6)

generate.generateImage(coeffs, 1000, 1000)

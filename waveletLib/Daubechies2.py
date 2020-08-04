class Daubechies2(Wavelet):
    def __init__(self):
        self._name = "Daubechies 2";
        self._motherWavelength = 4;
        self._transformWavelength = 2;
        sqrt3 = 3 ** 0.5
        sqrt2 = 2 ** 0.5
        self._scalingDeCom = [(1 + sqrt3)/(4 * sqrt2), (3 + sqrt3)/(4 * sqrt2, (3 - sqrt3)/(4 * sqrt2, (1-sqrt3)/(4 * sqrt2]
        buildOrthonormalSpace(self)

class Wavelet:
    def __init__(self):
        self._name = None;
        self._motherWavelength = 0;
        self._transformWavelength = 0;
        self._scalingDeCom = None;
        self._waveletDeCom = None;
    # length in NOT ALWAYS len(signal) since we might be working to part of the array
    def decompose(self, signal, length):
        arrHilb = [0] * length
        h = length // 2
        for i in range(0, h):
            arrHilb[i] = 0
            arrHilb[i + h] = 0
            for j in range(0, self._motherWavelength):
                k = i*2 + j
                while k >= len(arrHilb):
                    k -= len(arrHilb)

                arrHilb[ i ] += signal[k] * self._scalingDeCom[ j ]
                arrHilb[ i + h ] += signal[ k ] * self._waveletDeCom[ j ]
        return arrHilb
    def _buildOrthonormalSpace(self):
        self._waveletDeCom = [0] * self._motherWavelength
        for i in range(0, self._motherWavelength):
            if i % 2 == 0:
                self._waveletDeCom[i] = self._scalingDeCom[ (self._motherWavelength - 1) - i]
            else:
                self._waveletDeCom[i] = - self._scalingDeCom[ (self._motherWavelength - 1) - i]

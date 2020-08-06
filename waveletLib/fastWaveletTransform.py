class FastWaveletTransform:
    def __init__(self, wavelet):
        self.wavelet = wavelet
    def decompose(self, signal, level):
        if level < 0:
            raise Exception("Level too low (can't be negative)")
        if 2 ** level > len(signal):
            raise Exception("Level too high")
        arrHilb = signal.copy()
        l = 0
        h = len(signal)
        transformWavelength = self.wavelet._transformWavelength
        while h >= transformWavelength and l < level:
            arrTempPart = self.wavelet.decompose(arrHilb, h)
            arrHilb = arrTempPart + arrHilb[len(arrTempPart):]
            h = h // 2
            l += 1
        return arrHilb

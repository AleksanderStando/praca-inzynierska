class FastWaveletTransform:
    def __init__(self, wavelet):
        self.wavelet = wavelet
    def decompose(self, signal, level):
        if level < 0 or 2 ** level > len(signal):
            raise Exception("Wrong level value")
        arrHilb = signal.copy()
        l = 0
        h = len(singal)
        transformWavelength = self.wavelet.transformWavelength
        while h >= transformWavelength and l < level:
            arrTempPart = _wavelet.decompose(arrHilb, h)
            arrHilb = arrTempPart ++ arrHilb[len(arrTempPart):]
            h = h // 2
            l += 1
        return arrHilb

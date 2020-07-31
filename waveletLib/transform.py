class Transform:
    def __init__(self, wavelet):
        self.wavelet = wavelet
    def decompose(self, signal, level):
        self.wavelet.decompose(signal, level)

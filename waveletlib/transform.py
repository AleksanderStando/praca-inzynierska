from util import *

class Transform:
    def __init__(self, wavelet):
        self.wavelet = wavelet
    def decompose(self, signal, level):
        if(len(signal) < 2**level):
            raise Exception("Level is too high for this length of data")
        coeffs_list = []
        a = signal
        for i in range(level):
            a, d = self.dwt(a)
            coeffs_list.append(d)

        coeffs_list.append(a)
        coeffs_list.reverse()
        return coeffs_list
        
    def dwt(self, data):
        cA = downsampling_convolution(self, data, self.wavelet.dec_lo, self.wavelet.step, "SYMMETRIC")
        cD = downsampling_convolution(self, data, self.wavelet.dec_hi, self.wavelet.step, "SYMMETRIC")
        return cA, cD

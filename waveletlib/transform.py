from util import *
from dataTooShortException import DataTooShortException

class Transform:
    def __init__(self, wavelet):
        self.wavelet = wavelet
    def decompose(self, signal, max_level, mode="SYMMETRIC"):
        if(len(signal) < 2**max_level):
            raise DataTooShortException("Level is too high for this length of data")
        coeffs_list = []
        a = signal
        for i in range(max_level):
            a, d = self.dwt(a, mode)
            coeffs_list.append(d)

        coeffs_list.append(a)
        coeffs_list.reverse()
        return coeffs_list

    def dwt(self, data, mode):
        cA = downsampling_convolution(self, data, self.wavelet.dec_lo, self.wavelet.step, mode)
        cD = downsampling_convolution(self, data, self.wavelet.dec_hi, self.wavelet.step, mode)
        return cA, cD

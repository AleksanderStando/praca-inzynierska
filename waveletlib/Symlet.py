import wavelet

class Symlet(wavelet.Wavelet):
    #TODO: przenieść mapę do osobnej klasy
    map = {
        2: [ 0.48296291314469025, 0.83651630373746899, 0.22414386804185735, -0.12940952255092145],
        3: [0.33267055295095688, 0.80689150931333875, 0.45987750211933132, -0.13501102001039084, -0.085441273882241486, 0.035226291882100656]
    }
    def __init__(self, order):
        self.dec_lo = [0] * (order * 2)
        self.dec_hi = [0] * (order * 2)
        self.dec_len = order*2
        self.family_name = "Symlet";
        self.short_name = "sym"
        self.support_width = 2*order - 1
        self.step = 2
        coeffs = self.map.get(order)
        for i in range(0, order * 2):
            self.dec_lo[i] = coeffs[2*order - 1 - i]
            self.dec_hi[i] = coeffs[i]* self.is_even(2*order-1-i)
    def is_even(self, number):
        if number % 2 == 0:
            return 1
        else:
            return -1

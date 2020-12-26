import wavelet

class Coiflet(wavelet.Wavelet):
    #TODO: przenieść mapę do osobnej klasy
    map = {
            1: [-0.0727326195128539,
            0.3378976624578092,
            0.8525720202122554,
            0.38486484686420286,
            -0.0727326195128539,
            -0.01565572813546454],
        2: [-0.0007205494453645122,
            -0.0018232088707029932,
            0.0056114348193944995,
            0.023680171946334084,
            -0.0594344186464569,
            -0.0764885990783064,
            0.41700518442169254,
            0.8127236354455423,
            0.3861100668211622,
            -0.06737255472196302,
            -0.04146493678175915,
            0.016387336463522112
            ],
    }
    def __init__(self, order):
        self.dec_lo = [0] * (order * 6)
        self.dec_hi = [0] * (order * 6)
        self.dec_len = order*6
        self.family_name = "Coiflet";
        self.short_name = "co"
        self.support_width = 6*order - 1
        self.step = 2
        coeffs = self.map.get(order)
        for i in range(0, order * 6):
            self.dec_lo[i] = coeffs[6*order - 1 - i]
            self.dec_hi[i] = coeffs[i]* self.is_even(6*order-1-i)
    def is_even(self, number):
        if number % 2 == 0:
            return 1
        else:
            return -1

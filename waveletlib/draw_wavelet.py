import matplotlib.pyplot as plt

def draw_wavelet(wavelet):
    x_scale = range(wavelet.dec_len)
    plt.figure()
    plt.subplot(211)
    plt.plot(x_scale, wavelet.dec_hi, "ro")
    plt.axis([-1, len(x_scale), -2, 2])
    plt.grid(True, axis='y')
    plt.title('Decomposition high-pass filter')
    plt.subplot(212)
    plt.plot(x_scale, wavelet.dec_lo, "go")
    plt.axis([-1, len(x_scale), -2, 2])
    plt.grid(True, axis='y')
    plt.title('Decomposition low-pass filter')
    plt.subplots_adjust(left=0.10, right=0.95, hspace=0.70,
                    wspace=0.35)
    plt.show()

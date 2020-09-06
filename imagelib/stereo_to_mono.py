import os
from scipy.io import wavfile
import sys
import numpy as np

def stereo_to_mono(dir_name):
    for filename in os.listdir(dir_name):
        samplerate, data = wavfile.read(dir_name + '/' + filename)
        print(type(data[0]))
        print(data)
        if isinstance(data[0], np.ndarray):
            data = data.sum(axis=1) // 2
            data = data.astype(np.int16)
            print(data)
            wavfile.write(dir_name + '/' + filename, samplerate, data)

stereo_to_mono("Cut_Data/House-Sparrow-WAV")

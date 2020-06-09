import pywt
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
from PIL import Image

def pywt_example():
    x = [3, 7, 1, 1, -2, 5 ,4, 6, 6, 4, 5, -2, 1, 1, 7, 3]

    coeffs = pywt.wavedec(x, 'db1', level=2, mode='periodic')
    cA2, cD2, cD1 = coeffs

    print("cA2=", cA2)
    print("cD2=", cD2)
    print("cD1=", cD1)

def WAV_example():
    samplerate, data = wavfile.read("file_example_WAV_1MG.wav");
    data = data[:, 0]
    t = np.arange(len(data)/float(samplerate))
    data = data/max(data)
    max_level =  pywt.dwt_max_level(len(data), 'sym5')
    print("Max level: ", max_level)
    cA3, cD3, cD2, cD1 = pywt.wavedec(data, 'sym5', level = 3)
    wavfile.write("exampleD3.wav", samplerate, cD3)
    wavfile.write("exampleD2.wav", samplerate, cD2)
    wavfile.write("exampleD1.wav", samplerate, cD1)
    wavfile.write("exampleA3.wav", samplerate, cA3)
    return t, data, cD3, cD2, cD1, cA3

def findMax(data):
    max = -1
    for item in data:
        for elem in item:
            if elem > max:
                max = elem
    return max

def printPlot():
    t, data, cD3, cD2, cD1, cA3 = WAV_example()

    plt.figure(figsize=(30,20))

    plt.subplot(4,1,1)
    plt.plot(data, color='k')
    plt.xlabel('Time')
    plt.ylabel('S')
    plt.title('Original Signal')

    plt.subplot(4,1,2)
    plt.plot(cD3, color='g')
    plt.xlabel('Samples')
    plt.ylabel('cD3')
    plt.title('cD3')

    plt.subplot(4,1,3)
    plt.plot(cD2, color='g')
    plt.xlabel('Samples')
    plt.ylabel('cD2')
    plt.title('cD2')

    plt.subplot(4,1,4)
    plt.plot(cD1, color='g')
    plt.xlabel('Samples')
    plt.ylabel('cD1')
    plt.title('cD1')
    plt.show()

def printEnergyMap():
    t, data, cD3, cD2, cD1, cA3 = WAV_example()
    cD3 = cD3.tolist()
    cD2 = cD2.tolist()
    cD1 = cD1.tolist()
    cD3 = multiplyList(cD3, 4)
    cD2 = multiplyList(cD2, 2)
    cD3 = scaleList(cD3, 200)
    cD2 = scaleList(cD2, 200)
    cD1 = scaleList(cD1, 200)
    #print(cD2)

    max = getMax([cD3, cD2, cD1])
    min = getMin([cD3, cD2, cD1])
    scaleLevel = 255/(max-min)

    cD1 = [int((elem-min)*scaleLevel) for elem in cD1]
    cD2 = [int((elem-min)*scaleLevel) for elem in cD2]
    cD3 = [int((elem-min)*scaleLevel) for elem in cD3]

    print(cD1)
    print(cD2)
    print(cD3)

    img_arr = [cD1 for i in range(30)] + [cD2 for i in range(30)] + [cD3 for i in range(30)]
    img_numpy = np.array(img_arr).astype(np.uint8)
    img = Image.fromarray(img_numpy)
    img.save("example.png")

def getMax(list_of_lists):
    mx = None
    for list in list_of_lists:
        print(list)
        if mx is None or max(list) > mx:
            mx = max(list)
    return mx

def getMin(list_of_lists):
    mn = None
    for list in list_of_lists:
        if mn is None or min(list) < mn:
            mn = min(list)
    return mn

def scaleList(lst, size):
    batch = len(lst) // size
    new_list = []
    for i in range(size):
        table = lst[i*batch: min((i+1)*batch, len(lst))]
        item = statistics.mean(table)
        new_list.append(item)
    return new_list

# lst = [1,2,3], times = 2 --> [1,1,2,2,3,3]
def multiplyList(lst, times):
    new_list = []
    for item in lst:
        for i in range(times):
            new_list.append(item)

    return new_list

printEnergyMap()

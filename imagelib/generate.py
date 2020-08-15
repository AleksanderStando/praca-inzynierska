import statistics
from scipy.interpolate import interp1d
import numpy as np
import math
from PIL import Image

# na wyjściu - lista współczynników detali otrzymanych z filtra, pierwszy element listy to współczynnik aproksymacji
def generateImage(coeffs, x, y):
    # odrzucamy niepotrzeby współczynnik aproksymacji
    coeffs = coeffs[1:]
    level = len(coeffs)

    maxVal = getMax(coeffs)
    minVal = getMin(coeffs)
    scale_level = 255/(maxVal-minVal)
    # zamiana listy na postać, która umożliwia stworzenie obrazka
    # wyrównanie list do równej długości
    for i in range(0, level):
        coeffs[i] = multiplyList(coeffs[i], 2**(level-1-i))
        coeffs[i] = scale_list(coeffs[i], x)
        coeffs[i] = [int((elem-minVal)*scale_level) for elem in coeffs[i]]
    #print(coeffs)

    y_scale = max(1, y // level)
    img_ready_table = prepare_table(coeffs, y_scale)

    img_numpy = np.array(img_ready_table).astype(np.uint8)
    img = Image.fromarray(img_numpy)
    img.save("example.png")

def prepare_table(coeffs, scale):
    table = []
    for lst in coeffs:
        for i in range(scale):
            table.append(lst)
    return table

def multiplyList(lst, times):
    new_list = []
    for item in lst:
        for i in range(times):
            new_list.append(item)

    return new_list

def scale_list(lst, size):
    x_size = len(lst)
    x = np.linspace(0, size-1, num=x_size, endpoint=True)
    y = np.array(lst)

    f1 = interp1d(x, y)
    return [f1(i) for i in range(size)]

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

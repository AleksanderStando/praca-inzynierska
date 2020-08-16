import statistics
from scipy.interpolate import interp1d
import numpy as np
import math
from PIL import Image
from matplotlib import cm

# na wyjściu - lista współczynników detali otrzymanych z filtra, pierwszy element listy to współczynnik aproksymacji
def generateImage(coeffs, x, y, filename):
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

    y_scale = max(1, y // level)
    img_ready_table = prepare_table(coeffs, y_scale)

    img = Image.fromarray(np.uint8(cm.gist_earth(img_ready_table)*255))
    img.save(filename + ".png")

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
        if mx is None or max(list) > mx:
            mx = max(list)
    return mx

def getMin(list_of_lists):
    mn = None
    for list in list_of_lists:
        if mn is None or min(list) < mn:
            mn = min(list)
    return mn

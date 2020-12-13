import statistics
from scipy.interpolate import interp1d
import numpy as np
import math
from PIL import Image
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib
from matplotlib.colors import TwoSlopeNorm

def showImage(plt):
    plt
    plt.show()

def saveImage(plt, filename):
    matplotlib.pyplot.savefig(filename)
    plt.clf()

def prepare_standard_scale(max_value):
    return lambda x: int(x*(175/max_value))

def prepare_log_scale(max_value):
    log_scale = math.pow(max_value, 1/175)
    print("Log scale")
    print(log_scale)
    return lambda x: int(math.log(x, log_scale))

def get_color(value, scale_pos, scale_neg):
    if value == 0:
        return [0,0,0]
    elif value > 0:
        return [int(scale_pos(value)), 0, 0]
    elif value < 0:
        return [0, int(scale_neg(-value)), 0]

def generateImage(coeffs, x, y, filename, log_scale = False, time = 10):
    # odrzucamy niepotrzeby współczynnik aproksymacji
    coeffs = coeffs[1:]
    level = len(coeffs)

    maxVal = getMax(coeffs)
    minVal = getMin(coeffs)

    # zamiana listy na postać, która umożliwia stworzenie obrazka
    # wyrównanie list do równej długości
    for i in range(0, level):
        coeffs[i] = multiplyList(coeffs[i], 2**(level-1-i))
        coeffs[i] = scale_list(coeffs[i], x)

    y_scale = max(1, y // level)
    img_ready_table = prepare_table(coeffs, y_scale)
    Z = np.array(img_ready_table)
    Z = np.rot90(Z, 3)

    Y_SIZE = len(img_ready_table)
    X_SIZE = len(img_ready_table)

    step_x = time/X_SIZE
    step_y = level/Y_SIZE

    X, Y = np.mgrid[0:time:complex(0, X_SIZE), 0:level:complex(0, Y_SIZE)]

    fig, ax = plt.subplots(1, 1)
    if log_scale==True:
        pcm = ax.pcolormesh(X, Y, Z, norm=colors.SymLogNorm(linthresh=100, linscale=1,
                                vmin=Z.min(), vmax=Z.max(), base=10), cmap='RdBu_r', shading='auto')
    else:
        norm = TwoSlopeNorm(vmin=Z.min(), vcenter=0, vmax=Z.max())
        pcm = ax.pcolormesh(X,Y,Z, cmap='RdBu_r', shading='auto', norm = norm)

    fig.colorbar(pcm, ax=ax, extend='both')

    plt.xlabel("Time [s]")
    plt.ylabel("Level")
    return plt

    #img = Image.fromarray(np.uint8(cm.gist_earth(img_ready_table)*255))
    #img.save(filename + ".png")

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

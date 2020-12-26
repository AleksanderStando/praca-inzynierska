import numpy as np
import characteristic
from levelTooSmallException import *

class LevelAvgAmp(characteristic.Characteristic):
    #data_level - from which level do we take data
    def __init__(self,data_level, min_time):
        self.data_level = data_level
        self.min_time = min_time

    def checkLevel(self, levels):
        if levels < self.data_level:
            raise LevelTooSmallException("Data is decomposed to too little amount of levels")

    def calculate(self, data, time):
        self.check_time(time)
        data = data[1:]
        self.checkLevel(len(data))

        maxVal = self.getMax(data)

        data = data[-self.data_level]
        data = [abs(elem) for elem in data]

        scale_level = 1/maxVal
        data = [elem*scale_level for elem in data]

        avg = sum(data)/len(data)
        return avg

    def getAvg(self, list_of_lists):
        return np.sum(list_of_lists) / np.size(list_of_lists)

    def getMax(self, list_of_lists):
        mx = None
        for list in list_of_lists:
            if mx is None or max(list) > mx:
                mx = max(list)
        return mx

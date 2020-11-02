import numpy as np
import characteristic

class LevelVar(characteristic.Characteristic):
    #data_level - from which level do we take data
    #data cut - which % of data do we cut
    def __init__(self,importance, data_level, min_time, data_cut, window_time, slide_time):
        self.importance = importance
        self.data_level = data_level
        self.data_cut = data_cut
        self.window_time = window_time
        self.slide_time = slide_time
        self.min_time = min_time

    def checkLevel(self, levels):
        if levels < self.data_level:
            raise Exception("Data is decomposed to too little amount of levels")

    def calculate(self, data, time):
        self.check_time(time)
        data = data[1:]
        self.checkLevel(len(data))


        maxVal = self.getMax(data)
        minVal = self.getMin(data)

        scale_level = 1/(maxVal-minVal)

        data = data[-self.data_level]
        data = [(elem-minVal)*scale_level for elem in data]

        start = 0
        stop = self.window_time
        max_score = 0
        while(stop < time):
            score = self.getScore(data[int(len(data)*start/time):int(len(data)*stop/time)])
            if score > max_score:
                max_score = score
            stop += self.slide_time
            start += self.slide_time
        return max_score

    def getScore(self, data):
        data.sort()
        data = data[int(len(data)*self.data_cut/100):int(len(data)*(100-self.data_cut)/100)]
        return np.var(data)

    def getMax(self, list_of_lists):
        mx = None
        for list in list_of_lists:
            if mx is None or max(list) > mx:
                mx = max(list)
        return mx

    def getMin(self, list_of_lists):
        mn = None
        for list in list_of_lists:
            if mn is None or min(list) < mn:
                mn = min(list)
        return mn

import numpy as np

class TypeModel():
    def __init__(self, name, values):
        self.name = name
        self.avg = self.calc_avg(values)
        self.var = self.calc_var(values)
        self.min = self.calc_min(values)
        self.max = self.calc_max(values)
    def calc_var(self, values):
        return np.var(values)
    def calc_avg(self, values):
        return np.mean(values)
    def calc_min(self, values):
        return np.min(values)
    def calc_max(self,values):
        return np.max(values)

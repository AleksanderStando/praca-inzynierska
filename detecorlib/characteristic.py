from dataTooShortException  import *

class Characteristic:
    def __init__(self, min_time):
        self.min_time = min_time
    def check_time(self, time):
        if time < self.min_time:
            raise DataTooShortException("Data isn't long enough to count characteristic score")

class CommonLoonType(DetectType):
    def __init__(self):
        self.name = "Common Loon"
        self.min_level = 5
        self.min_length = 1000
        self.characteristics = None
    def calculate(self, data, time):
        score = 0
        total_importance = 0
        for c in self.characteristics:
            score += c.calculate(data, time) * c.importance
            total_importance += c.importance
        return score/total_importance

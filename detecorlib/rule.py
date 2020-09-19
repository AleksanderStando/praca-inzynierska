class Rule:
    def __init__(self, char, threshold, passed, failed):
        self.char = char
        self.threshold = threshold
        self.passed_types = passed
        self.failed_types = failed
    def get_poss_types(self, data, time):
        score = self.char.calculate(data, time)
        if score >= self.threshold:
            return self.passed_types
        else:
            return self.failed_types

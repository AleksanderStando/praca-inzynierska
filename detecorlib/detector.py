class Detector:
    def __init__(self):
        self.types = []

    def add_type(self, type):
        self.types = self.types + [type]

    def recognize(self, data):
        results = {}
        for type in self.types:
            results[type.name] = type.calculate(data, time)
        return max(results, key=results.get)

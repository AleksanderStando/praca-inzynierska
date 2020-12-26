class Rule:
    def __init__(self, name, char, mode = "normal", weight = 1, checked = True):
        self.weight = weight
        self.name = name
        self.char = char
        self.mode = mode
        self.type_models = {}
        self.checked = checked

    def get_poss_types(self, data, time):
        score = self.char.calculate(data, time)
        if score >= self.threshold:
            return self.passed_types
        else:
            return self.failed_types

    def add_type_model(self, type_model):
        self.type_models[type_model.name] = type_model

    def check(self):
        self.checked = True

    def uncheck(self):
        self.checked = False

    def calculate(self, data, time):
        return self.char.calculate(data, time)

    def count_score(self, name, char_score):
        model = self.type_models[name]
        if self.mode == "normal":
            if char_score == model.avg:
                return 100
            if model.avg == 0:
                return 0
            if char_score > model.avg:
                scale = model.avg/char_score
            else:
                scale = char_score/model.avg
            scale_score = max(50*scale, 0)
            if char_score > model.avg:
                if model.max == model.avg:
                    minmax_score = 0
                else:
                    minmax_score = max(50 - ((char_score - model.avg) / (model.max - model.avg) * 25), 0)
            else:
                if model.avg == model.min:
                    minmax_score = 0
                else:
                    minmax_score = max(50 - ((model.avg - char_score) / (model.avg - model.min) * 25), 0)
            return scale_score + minmax_score

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

    def count_score(self,name, char_score):
        model = self.type_models[name]
        if self.mode == "normal":
            if char_score == model.avg:
                return 100
            diff = abs(model.avg - char_score)
            tolerated_diff = 3*model.var
            if tolerated_diff == 0:
                return 0
            var_score = max(50 - (diff*50 / tolerated_diff), 0)
            if char_score > model.avg:
                minmax_score = max(50 - ((char_score - model.avg) / (model.max - model.avg) * 25), 0)
            else:
                minmax_score = max(50 - ((model.avg - char_score) / (model.avg - model.min) * 25), 0)
            return var_score + minmax_score

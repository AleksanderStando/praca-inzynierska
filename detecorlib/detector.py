class Detector:
    def __init__(self, rules, types):
        self.types = types
        self.rules = rules

    def add_type(self, type):
        self.types = self.types + [type]

    def add_rule(self, rule):
        self.rules = self.rules + [rule]

    def recognize(self, data, time):
        poss_types = self.types
        for rule in self.rules:
            rule_types = rule.get_poss_types(data, time)
            #print(poss_types)
            #print(rule_types)
            poss_types = [value for value in poss_types if value in rule_types]
            if len(poss_types) == 1:
                return poss_types[0]
            if len(poss_types) == 0:
                return "No type found"
        return "Couldn't detect type"

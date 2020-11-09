import os
import sys
from type_model import TypeModel
sys.path.insert(0, '../serializelib')
from serialization import *

class Detector:
    def __init__(self, rules):
        self.rules = rules

    def add_rule(self, rule):
        self.rules = self.rules + [rule]

    def calculate_rules(self, path):
        result_dict = {}
        types = []
        for folder in os.listdir(path):
            type_name = folder
            types.append(type_name)
            for rule in self.rules:
                result_dict[(rule.name, type_name)] = []
            inner_folder = os.path.join(path, folder)
            for file in os.listdir(inner_folder):
                coeffs, time, name, family, order = deserialize(inner_folder, file)
                for rule in self.rules:
                    res = rule.char.calculate(coeffs, time)
                    print(res)
                    result_dict[(rule.name, type_name)].append(res)
        print(result_dict)
        self.types = types
        for rule in self.rules:
            for type in self.types:
                type_model = TypeModel(type, result_dict[(rule.name, type)])
                rule.add_type_model(type_model)
        for rule in self.rules:
            print(rule.type_models)

    def recognize(self, data, time):
        types = self.types
        result = {}
        for rule in self.rules:
            char_score = rule.char.calculate(data, time)
            for type in types:
                rule_score = rule.count_score(type, char_score)
                result[(rule.name, type)] = rule_score
        max_score = -1
        result_type = ""
        for type in types:
            rec_score = 0
            for rule in self.rules:
                rec_score = rec_score + result[(rule.name, type)]
            print(str(type) + " " + str(rec_score))
            if rec_score > max_score:
                result_type = type
                max_score = rec_score
        return result_type

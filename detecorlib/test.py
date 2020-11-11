import sys
from scipy.io import wavfile
import os
from level_var import LevelVar
from level_spikes import LevelSpikes
from detector import Detector
from rule import Rule

sys.path.insert(0, '../waveletlib')
sys.path.insert(0, '../serializelib')
from transform import Transform
from Daubechies import Daubechies
from serialization import *


wave = Transform(Daubechies(3))

def test_characteristic(path, char):
    for filename in os.listdir(path):
        samplerate, data = wavfile.read(os.path.join(path, filename))
        print(samplerate)
        coeffs = wave.decompose(data, 10)
        score = char.calculate(coeffs, 10000)
        print(path + " " + filename + " " + str(score))

#test_characteristic(os.path.join("Cut_Data", "Common-Loon-WAV"), level_5_var_char)
#test_characteristic(os.path.join("Cut_Data", "Eurasian-Skylark-WAV"), level_3_spikes_char)
#test_characteristic(os.path.join("Cut_Data", "House-Sparrow-WAV"), level_3_spikes_char)

def serialize_folder(path, save_folder):
    for filename in os.listdir(path):
        samplerate, data = wavfile.read(os.path.join(path, filename))
        time = int(len(data)*1000/samplerate)
        coeffs = wave.decompose(data, 5)
        serialize(save_folder, coeffs, time, filename, wave.wavelet.family_name, wave.wavelet.dec_len)

def test_system(detector, path):
    correct_ans_total = 0
    sum_ans_total = 0
    for folder in os.listdir(path):
        correct_ans = 0
        sum_ans = 0
        expected_res = folder
        inner_folder = os.path.join(path, folder)
        for file in os.listdir(inner_folder):
            coeffs, time, name, family, order = deserialize(inner_folder, file)
            result = detector.recognize(coeffs, time)
            print("Expected answer: " + expected_res + ", detector answer: " + result)
            if result == expected_res:
                correct_ans += 1
            sum_ans += 1
        print("Correct answers: " + str(correct_ans) + ", incorrect answers: " + str(sum_ans-correct_ans) + " for type: " + str(expected_res))
        correct_ans_total = correct_ans_total + correct_ans
        sum_ans_total = sum_ans_total + sum_ans
    print("Final results: ")
    print("Correct answers: " + str(correct_ans_total) + ", incorrect answers: " + str(sum_ans_total-correct_ans_total))
    return (correct_ans_total, sum_ans_total)

def train_detector_serialized(detector, path):
    detector.calculate_rules(path)

common_loon = "Common Loon"
eurasian_skylark = "Eurasian Skylark"
house_sparrow = "House Sparrow"

level_5_var_char = LevelVar(5, 3000, 0, 3000, 300)
level_4_var_char = LevelVar(4, 3000, 0, 3000, 300)
level_3_var_char = LevelVar(3, 3000, 0, 3000, 300)
level_3_spikes_char = LevelSpikes(3, 3000, 500, 300, 1.1)
level_2_spikes_char = LevelSpikes(2, 3000, 500, 300, 1.1)

rule1 = Rule("level5var", level_5_var_char)
rule2 = Rule("level4var", level_4_var_char)
rule3 = Rule("level3var", level_3_var_char)
rule4 = Rule("level3spikes", level_3_spikes_char)
rule5 = Rule("level2spikes", level_2_spikes_char)

bird_detector = Detector([rule1, rule2, rule3, rule4, rule5])

#serialize_folder(os.path.join("Cut_Data", "Common-Loon-WAV"), "Common-Loon-Serialized")
#serialize_folder(os.path.join("Cut_Data", "Eurasian-Skylark-WAV"), "Eurasian-Skylark-Serialized")
#serialize_folder(os.path.join("Cut_Data", "House-Sparrow-WAV"), "House-Sparrow-Serialized")

train_detector_serialized(bird_detector, "serialized_train")
test_system(bird_detector, "serialized_test")

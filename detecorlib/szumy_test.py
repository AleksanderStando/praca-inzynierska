import sys
from scipy.io import wavfile
import os
from level_var import LevelVar
from level_spikes import LevelSpikes
from level_avg_amp import LevelAvgAmp
from detector import Detector
from rule import Rule

sys.path.insert(0, '../waveletlib')
sys.path.insert(0, '../serializelib')
from transform import Transform
from Daubechies import Daubechies
from serialization import *


wave = Transform(Daubechies(3))

def test_characteristic(path, char):
    sum = 0
    count = 0
    for filename in os.listdir(path):
        coeffs, time, name, family, order = deserialize(path, filename)
        score = char.calculate(coeffs, time*1000)
        #print(path + " " + filename + " " + str(score))
        sum = sum + score
        count = count + 1
    print(path + "Avg " + str((sum/count)))

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
            print(time)
            result, rules_map = detector.recognize(coeffs, time*1000)
            print("Expected answer: " + expected_res + ", detector answer: " + result)
            print(rules_map)
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

mycie_zebow = "mycie_zebow"
ocean = "ocean"
wiatr = "wiatr"

level_1 = LevelAvgAmp(1, 3000)
level_2 = LevelAvgAmp(2, 3000)
level_3 = LevelAvgAmp(3, 3000)
level_4 = LevelAvgAmp(4, 3000)
level_5 = LevelAvgAmp(5, 3000)
level_6 = LevelAvgAmp(6, 3000)
level_7 = LevelAvgAmp(7, 3000)
level_8 = LevelAvgAmp(8, 3000)
level_9 = LevelAvgAmp(9, 3000)
level_10 = LevelAvgAmp(10, 3000)

level_1_var = LevelVar(1, 3000, 0, 3000, 300)
level_2_var = LevelVar(2, 3000, 0, 3000, 300)
level_3_var = LevelVar(3, 3000, 0, 3000, 300)
level_4_var = LevelVar(4, 3000, 0, 3000, 300)
level_5_var = LevelVar(5, 3000, 0, 3000, 300)
level_6_var = LevelVar(6, 3000, 0, 3000, 300)
level_7_var = LevelVar(7, 3000, 0, 3000, 300)
level_8_var = LevelVar(8, 3000, 0, 3000, 300)
level_9_var = LevelVar(9, 3000, 0, 3000, 300)
level_10_var = LevelVar(10, 3000, 0, 3000, 300)

rule1 = Rule("level1", level_1)
rule2 = Rule("level2", level_2)
rule3 = Rule("level3", level_3)
rule4 = Rule("level4", level_4)
rule5 = Rule("level5", level_5)
rule6 = Rule("level6", level_6)
rule7 = Rule("level7", level_7)
rule8 = Rule("level8", level_8)
rule9 = Rule("level9", level_9)
rule10 = Rule("level10", level_10)

rule1var = Rule("level1var", level_1_var)
rule2var = Rule("level2var", level_2_var)
rule3var = Rule("level3var", level_3_var)
rule4var = Rule("level4var", level_4_var)
rule5var = Rule("level5var", level_5_var)
rule6var = Rule("level6var", level_6_var)
rule7var = Rule("level7var", level_7_var)
rule8var = Rule("level8var", level_8_var)
rule9var = Rule("level9var", level_9_var)
rule10var = Rule("level10var", level_10_var)

szum_detector = Detector([rule1var, rule3var, rule5var, rule7var, rule9var, rule2, rule4, rule6, rule8, rule10])

#serialize_folder(os.path.join("Cut_Data", "Common-Loon-WAV"), "Common-Loon-Serialized")
#serialize_folder(os.path.join("Cut_Data", "Eurasian-Skylark-WAV"), "Eurasian-Skylark-Serialized")
#serialize_folder(os.path.join("Cut_Data", "House-Sparrow-WAV"), "House-Sparrow-Serialized")

train_detector_serialized(szum_detector, "szumy_train")
test_system(szum_detector, "szumy_test")

#test_characteristic("szumy_train/mycie_zebow", level_10)
#test_characteristic("szumy_train/ocean", level_10)
#test_characteristic("szumy_train/wiatr", level_10)

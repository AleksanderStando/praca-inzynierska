import sys
from scipy.io import wavfile
import os
from level_var import LevelVar
from level_spikes import LevelSpikes
from detector import Detector
from rule import Rule

sys.path.insert(0, '../waveletlib')
from transform import Transform
from Daubechies import Daubechies


wave = Transform(Daubechies(3))

level_5_var_char = LevelVar(1, 5, 0, 3000, 300)
level_3_spikes_char = LevelSpikes(1, 3, 3000, 300, 1.10)

def test_characteristic(path, char):
    for filename in os.listdir(path):
        samplerate, data = wavfile.read(os.path.join(path, filename))
        coeffs = wave.decompose(data, 10)
        score = char.calculate(coeffs, 10000)
        print(path + " " + filename + " " + str(score))

#test_characteristic(os.path.join("Cut_Data", "Common-Loon-WAV"), level_5_var_char)
#test_characteristic(os.path.join("Cut_Data", "Eurasian-Skylark-WAV"), level_3_spikes_char)
#test_characteristic(os.path.join("Cut_Data", "House-Sparrow-WAV"), level_3_spikes_char)

def test_system(detector, path, expected_answer):
    correct_ans = 0
    sum_ans = 0
    for filename in os.listdir(path):
        samplerate, data = wavfile.read(os.path.join(path, filename))
        coeffs = wave.decompose(data, 10)
        answer = detector.recognize(coeffs, 10000)
        print("Expected answer: " + expected_answer + ", actual answer: " + answer)
        if answer == expected_answer:
            correct_ans += 1
        sum_ans += 1
    print("Correct answers: " + str(correct_ans) + ", incorrect answers: " + str(sum_ans-correct_ans))
    return (correct_ans, sum_ans)

common_loon = "Common Loon"
eurasian_skylark = "Eurasian Skylark"
house_sparrow = "House Sparrow"

rule1 = Rule(level_5_var_char, 0.001, [common_loon], [eurasian_skylark, house_sparrow])
rule2 = Rule(level_3_spikes_char, 0.1, [eurasian_skylark, common_loon], [house_sparrow, common_loon])

bird_detector = Detector([rule1, rule2], [common_loon, eurasian_skylark, house_sparrow])

test_system(bird_detector, os.path.join("Cut_Data", "Common-Loon-WAV"), common_loon)
test_system(bird_detector, os.path.join("Cut_Data", "Eurasian-Skylark-WAV"), eurasian_skylark)
test_system(bird_detector, os.path.join("Cut_Data", "House-Sparrow-WAV"), house_sparrow)

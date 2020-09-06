import sys
from scipy.io import wavfile

def cut_file(file, start, time, new_file):
    samplerate, data = wavfile.read(file)
    print(data)
    # wycinamy plik od sekundy start, plik ma długość time
    data = data[samplerate*start:samplerate*(start+time)]
    wavfile.write(new_file, samplerate, data)

if len(sys.argv) < 4:
    raise NameError('You need to provide file_name, start_time, time_length')

name = sys.argv[1]
start = int(sys.argv[2])
time = int(sys.argv[3])
path = "Data/House-Sparrow-WAV/"
new_path = "Cut_Data/House-Sparrow-WAV/"
cut_file(path + name, start, time, new_path + name)

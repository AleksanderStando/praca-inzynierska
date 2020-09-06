import csv
import requests
import os
from pathlib import Path
from pydub import AudioSegment

def downloadSamples(file_path, folder_name):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if(row[1] == "Audio"):
                url = "" + row[-2] + row[0]
                print(url)
                file = requests.get(url)
                open(folder_name + '/' + row[0], 'wb').write(file.content)
#downloadSamples('House-Sparrow.csv', "House-Sparrow-mp3")
#downloadSamples('Common-Loon.csv', 'Common-Loon-mp3')
#downloadSamples('Eurasian-Skylark.csv', 'Eurasian-Skylark-mp3')

def convertMp3ToWav(mp3_folder, wav_folder, prefix):
    Path(wav_folder).mkdir(parents=True, exist_ok=True)
    for file in os.listdir(mp3_folder):
        print(file)
        sound = AudioSegment.from_mp3(os.path.join(mp3_folder, file))
        sound.export(os.path.join(wav_folder, prefix+file), format="wav")

#convertMp3ToWav('Common-Loon-mp3', 'Common-Loon-WAV', 'CL_')
#convertMp3ToWav('House-Sparrow-mp3', 'House-Sparrow-WAV', 'HS_')
#convertMp3ToWav('Eurasian-Skylark-mp3', 'Eurasian-Skylark-WAV', 'ES_')

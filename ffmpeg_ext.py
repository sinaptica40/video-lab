import subprocess
import os
import glob
from pathlib import Path


def estrai_frame(video_path, secondi):
    base_name = Path(video_path).stem
    # Modifica il formato del timestamp nel nome del file
    output_file_name = f'{base_name}_secondo_{secondi.replace(":", "-")}.jpg'
    output_file = 'G:/VideoPack2/' + output_file_name

    command = [
        'C:\\ffmpeg-n6.0-latest-win64-lgpl-shared-6.0\\bin\\ffmpeg.exe',
        '-i', str(video_path),
        '-ss', secondi,
        '-frames:v', '1',
        str(output_file)
    ]

    print("Eseguendo il comando:", " ".join(command))
    print("Percorso del file di output:", output_file)

    subprocess.run(command)


cartella_video = 'G:/VideoPack2/'
secondi_da_estrarre = ['00:00:05', '00:00:07']
output_folder = Path('output_frames')

for video_file in glob.glob(cartella_video + '**/*.mp4', recursive=True):
    for secondo in secondi_da_estrarre:
        estrai_frame(video_file, secondo)

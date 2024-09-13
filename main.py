import os

from constants import AudioQualities
from converter import audio_converter
from create_directories import create_directories
from temp import create_temp
from concurrent.futures import ThreadPoolExecutor, as_completed

extensions = [".mp3"]

while True:
    path = os.path.dirname(os.path.abspath(__file__))

    audio_files = [file for file in os.listdir(path) if os.path.splitext(file)[1].lower() in extensions]

    if len(audio_files) == 0:
        print("please paste an audio file next to the project files.")
        break

    # print(os.listdir(path))
    # print(os.path.splitext(audio_files[0]))
    # print("*" * 100)
    else:
        for index, file in enumerate(audio_files):
            print(f"{index}:", file)

        selected = input("select audio file index: ")

        if not selected.isnumeric() or int(selected) > len(audio_files)-1:
            print("please inter valid index(number).")
        else:

            temp = create_temp()

            create_directories(temp.path)

            with ThreadPoolExecutor(max_workers=8) as pool:
                futures = [pool.submit(audio_converter, audio_files[int(selected)], temp.path, q) for q in
                           AudioQualities.directories()]
                for future in as_completed(futures):
                    pass
                    # print(future.result())

import os

from constants import AudioQualities
from path_manager import make_path


def create_directories(main_folder: str):
    for i in AudioQualities.directories():
        p = make_path(main_folder, i, is_file=False)
        if not os.path.exists(p):
            os.mkdir(p)

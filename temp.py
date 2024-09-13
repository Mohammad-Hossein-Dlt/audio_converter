import uuid
import os
import shutil

from path_manager import make_path


def init_temp_directory(directory_name: str):
    path = make_path(directory_name, is_file=False)
    if not os.path.exists(path):
        os.mkdir(path)
    return path


# def delete_temp(directory_name: str):
#     path = make_path(directory_name, is_file=False)
#     # if path.replace("/", "") != Directories.temp.replace("/", "") and os.path.exists(path):
#     if os.path.exists(path):
#         shutil.rmtree(path)
#         return path


class Temp:
    name: str
    path: str
    auto_delete: bool = True

    def __init__(self, name: str, path: str, auto_delete: bool = True):
        self.name = name
        self.path = path
        self.auto_delete = auto_delete

    # def delete(self):
    #     delete_temp(self.name)


def create_temp():
    name = uuid.uuid4().hex
    path = init_temp_directory(name)
    temp = Temp(name, path)

    return temp
    # try:
    #     yield temp
    # finally:
    #     delete_temp(name)

#
# def manual_delete_temp():
#     name = uuid.uuid4().hex
#     try:
#         path = init_temp_directory(name)
#         temp = Temp(name=name, path=path)
#         yield temp
#     finally:
#         pass

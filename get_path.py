import os


def download_relative_way(name_class, number, folderpath):
    return os.path.relpath(os.path.abspath(f"{folderpath}/{name_class}/{str(number).zfill(4)}.jpg"))


def changed_relative_way(name_class, number, folderpath):
    return os.path.relpath(f"{folderpath}/changed_dataset/{name_class}_{str(number).zfill(4)}.jpg")


def random_relative_way(number, folderpath):
    return os.path.relpath(f"{folderpath}/random_dataset/{str(number).zfill(4)}.jpg")


def get_absolute_way(name_class, number, mode, folderpath):
    if mode == "download":
        return os.path.abspath(f"{folderpath}/{name_class}/{str(number).zfill(4)}.jpg")
    if mode == "changed":
        return os.path.abspath(f"{folderpath}/changed_dataset/{name_class}_{str(number).zfill(4)}.jpg")
    if mode == "random":
        return os.path.abspath(f"{folderpath}/random_dataset/{str(number).zfill(4)}.jpg")

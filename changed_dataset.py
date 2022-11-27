import csv
import os
import get_path
import shutil
from typing import List


def copy_to_another(path: str, class_names: List[str], folderpath) -> None:
    """
    Функция копирует элелемент класса в другую директорию и записывает в аннотацию абсолютный, относительный пути
    и класс, к которому принадлежит копируемый элемент
    Args:
        file_writer (any): объект открытого файла аннотации
        class_names list(str): классы, к которому относится элемент
    """
    if not os.path.isdir("dataset/changed_dataset"):
        os.mkdir("dataset/changed_dataset")
    with open(path, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
        for class_name in class_names:
            for i in range(1, 1050):
                if (os.path.isfile(get_path.get_absolute_way(class_name, i, "download", folderpath)) == True):
                    shutil.copyfile(get_path.get_absolute_way(
                        class_name, i, "download", folderpath), get_path.get_absolute_way(class_name, i, "changed", folderpath))

                file_writer.writerow([get_path.get_absolute_way(
                    class_name, i, "download", folderpath), get_path.changed_relative_way(class_name, i, folderpath), class_name])


def main():
    print("Start changing")
    if not os.path.isdir("dataset/changed_dataset"):
        os.mkdir("dataset/changed_dataset")
    copy_to_another("changed_annotation.csv", ["rose", "tulip"])
    print("The end of changing")


if __name__ == "__main__":
    main()

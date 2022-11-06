import os
import get_path
import shutil
import csv
import random
from typing import List


def random_copy(path: str, class_names: List[str], folderpath) -> None:
    """
    Копирует элементы класса в другую директорию с рандомными именами от 0 до 10000(вне зависимости от класса изображения),
    и записывает в файл аннотацию абсолютный, относительный пути изображений, и класс к которому они относились
    Args:
        file_writer (any): объект открытого файла аннотации
        class_name (str): класс, к которому относится элемент
    """
    with open(path, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
        for class_name in class_names:
            for i in range(1050):
                rand_number = random.randint(0, 10000)
                if (os.path.isfile(get_path.get_absolute_way(class_name, i, "download", folderpath)) == True):
                    while (os.path.isfile(get_path.get_absolute_way(class_name, rand_number, "random", folderpath)) == True):
                        rand_number = random.randint(0, 10000)
                        
                    shutil.copyfile(get_path.get_absolute_way(
                        class_name, i, "download", folderpath), get_path.get_absolute_way(class_name, rand_number, "random", folderpath))
                    file_writer.writerow([get_path.get_absolute_way(
                        class_name, i, "download", folderpath), get_path.random_relative_way(rand_number, folderpath), class_name])


def main():
    print("Start")
    if not os.path.isdir("dataset/random_dataset"):
        os.mkdir("dataset/random_dataset")

    random_copy("random_annotation.csv", ["rose", "tulip"])
    print("The end")


if __name__ == "__main__":
    main()

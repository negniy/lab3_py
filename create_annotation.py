import csv
import os
import get_path
from typing import List


def create_annotation(path: str, class_names: List[str], folderpath) -> None:
    """
    Функция создает/открывает файл аннотацию и записывет в него Абсолютный, 
    относительный пути к данной фотографии и класс, к которому она относится

    Args:
        path (str): название файла аннотации
        class_names (List[str]): список типов класса
    """
    with open(path, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
        for class_name in class_names:
            for i in range(1050):
                if (os.path.isfile(get_path.get_absolute_way(class_name, i, "download", folderpath)) == True):
                    file_writer.writerow([get_path.get_absolute_way(
                        class_name, i, "download", folderpath), get_path.download_relative_way(class_name, i, folderpath), class_name])


def main():
    print("Start")
    create_annotation("annotation.csv", ["rose", "tulip"])
    print("The end")


if __name__ == "__main__":
    main()

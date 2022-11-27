import csv
import cv2
import matplotlib.pyplot as plt
import random
import pandas as pd


def create_dataframe():
    filename = 'annotation.csv'
    class_mark = []
    class_name =[]
    absolute_way = []
    with open(filename, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter = ";")
            for row in reader:
                if row[2]== 'rose':
                    class_mark.append(0)
                else :
                    class_mark.append(1)
                    
                class_name.append(row[2])
                absolute_way.append(row[0])
                
    dataframe = pd.DataFrame(
        {
            class_name[0]: pd.array(class_name[1:]),
            absolute_way[0]:  pd.array(absolute_way[1:]),
        }
    )
    
    print(dataframe.columns)
    print(dataframe)
    
    dataframe = dataframe.rename(
        columns={class_name[0]: 'class_name',
                 absolute_way[0]: 'absolute_way'}
        )
    
    dataframe['class_mark'] = pd.array(class_mark[1:])
    
    print(dataframe.columns)
    print(dataframe)

def main():
    print('program start')
    pd.set_option('display.max_colwidth', None)
    create_dataframe()
    print('program finish')
    
    
if __name__ == '__main__':
    main()
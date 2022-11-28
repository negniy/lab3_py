import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

def class_filter(dataframe, class_mark):
    res = pd.DataFrame(dataframe[dataframe.class_mark == class_mark])
    return res


def size_filter(dataframe, class_mark,  max_hight, max_width):
    res = pd.DataFrame(dataframe[dataframe.class_mark == class_mark][dataframe.hight <= max_hight][dataframe.width <= max_width])
    return res
  

def create():
    filename = "annotation.csv"
    class_mark = []
    class_name =[]
    absolute_way = []
    with open(filename, encoding="utf-8") as file:
            reader = csv.reader(file, delimiter = ";")
            for row in reader:
                if row[2]== "rose":
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
    
    dataframe = dataframe.rename(
        columns={class_name[0]: "class_name",
                 absolute_way[0]: "absolute_way"}
        )
    
    dataframe["class_mark"] = pd.array(class_mark[1:])
    
    hight = []
    width =[]
    depth = []
    
    for path in absolute_way:
        try:
            image = image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
            hight.append(image.shape[0])
            width.append(image.shape[1])
            depth.append(image.shape[2])
        except:
            pass
        
    dataframe["hight"] = pd.Series(hight)    
    dataframe["width"] = pd.Series(width)
    dataframe["depth"] = pd.Series(depth)
    
    print("\n Images hight statistic: \n")
    print(dataframe["hight"]. describe ())
    
    print("\n Images width statistic: \n")
    print(dataframe["width"]. describe ())
    
    print("\n Images depth statistic: \n")
    print(dataframe["depth"]. describe ())
    
    
    print("\n Filtrated dataframe(class): \n")
    print(class_filter(dataframe, 0))
    
    print("\n Filtrated dataframe(size and class): \n")
    print(size_filter(dataframe, 1, 400, 400))
    
    number_of_pixels = []
    
    for path in absolute_way:
        try:
            image = image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
            number_of_pixels.append(image.size)
        except:
            pass
        
    dataframe["number_of_pixels"] = pd.Series(number_of_pixels) 
    
    
    print(" \n Minimum number of pixels: \n ")
    print(dataframe.groupby("class_mark").number_of_pixels.min())
    
    print(" \n Maximum number of pixels: \n ")
    print(dataframe.groupby("class_mark").number_of_pixels.max())
    
    print(" \n The average value of the number of pixels: \n ")
    print(dataframe.groupby("class_mark").number_of_pixels.mean())
    
    
    print(dataframe.columns)
    print(dataframe)
    
    
    
    
    
    

def main():
    print("start")
    pd.set_option("display.max_colwidth", None)
    create()
    print("finish")
    
    
if __name__ == "__main__":
    main()
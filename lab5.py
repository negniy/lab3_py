import os
import glob
from PIL import Image
from typing import Tuple, Any
import numpy as np
import cv2
import csv
import pandas as pd
import torch
import torchvision
from torch.utils.data import Dataset
import matplotlib.pyplot as plt


class CustomImageDataset(Dataset):
    
    def __init__(self, file_list, transform: Any = None, target_transform: Any = None) -> None:
        self.file_list = file_list
        self.transform = transform
        self.target_transform = target_transform
        

    def __len__(self) -> int:
        self.filelength = len(self.file_list)
        return self.filelength
    
    #load an one of images
    def __getitem__(self, index: int) -> Tuple[torch.tensor, int]:
        path_to_image = self.file_list[index]
        image = Image.open(path_to_image)
        print(path_to_image)
    
        if 'rose' in path_to_image:
            label = 1
        elif 'tulip' in path_to_image:
            label = 0
        
        print(label)
        
        return image, label
         
            
        
    

def main():
    print('laba 5 started')
    
    images_list = []
    images_list = glob.glob(os.path.join('dataset/changed_dataset','*.jpg'))
    
    train_dataset = images_list[0 : int(len(images_list)*0.8)]
    test_dataset = images_list[int(len(images_list)*0.8) : int(len(images_list)*0.9)]
    val_dataset = images_list[int(len(images_list)*0.9) : int(len(images_list))]
    
    print(images_list)
    
    print(train_dataset)
    print(test_dataset)
    print(val_dataset)
    
    random_idx = np.random.randint(1,len(images_list),size=10)

    fig = plt.figure()
    i=1
    for idx in random_idx:
        fig.add_subplot(2,5,i)
        img = Image.open(images_list[idx])
        plt.imshow(img)
        i+=1
    
    plt.show()
    plt.axis('off')
    
    
    
    
    print('laba 5 ended')

if __name__ == '__main__':
    main()
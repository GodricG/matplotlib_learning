# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:12:04 2019

@author: Godric
"""


import os
import cv2
#生成包含所有目录的列表dir_pathlists
dir_pathlists = [os.sep.join(['d:\\test', os.listdir('d:/test/')[i]]) for i in range(len(os.listdir('d:/test/')))]
#定义获取目录下文件名的函数get_names
def get_names(path):
    filenames = [] #定义包含所有文件名的空列表filenames
    file_name_and_path = [] #包含所有文件名绝对路径的列表file_name_and_path
    for i in range(len(path)): #第一层循环，生成所有文件名的列表filenames
        filenames.append(os.listdir(path[i]))
        for j in range(len(os.listdir(path[i]))): #第二层循环，用os.sep.join函数将路径与文件名组合，以生成文件名绝对路径的列表
            file_name_and_path.append(os.sep.join([path[i], filenames[i][j]]))
    return file_name_and_path
x = get_names(dir_pathlists)

img = cv2.imread(x[-1])
print(x, x[-1])
cv2.imshow('dd', img)
cv2.waitKey()
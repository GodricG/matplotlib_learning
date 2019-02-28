# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:45:20 2019

@author: Godric
"""
import numpy as np
import cv2
n = 6000
canvas = np.zeros((1000, 600, 3), dtype = np.uint8) + 255
lamb = 2 * np.pi / n
angs = [[[np.cos(i * lamb), -np.sin(i * lamb)], [np.sin(i * lamb), np.cos(i * lamb)]] for i in range(1,n)]

rotas = np.array([[[0, -1]] + [np.dot(ang, [0, -1]) for ang in angs]], dtype = np.float)

points = np.round(rotas * 150 + np.array([300, 700])).reshape(n, 2).astype(np.int)
for i in range(n):
#    x = np.round(np.float(i)/n * 255)
#    y = np.round(np.float(i)/n * 255)
#    z = np.round(255-np.float(i)/n * 255)
    color_hsv = np.array([[[np.round(np.float(i)/n * 255), 255, 255]]]).astype(np.uint8)
    color = [int(c) for c in cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]]
    x = int(np.round(np.float(i)/n * 600))
    y = int(np.round(np.sin(np.pi / 180 * i / n * 600 * 15)))* 10
#    print(color_hsv, color)
#    z = np.round(128 - 1 * np.float(i)/n * 255) if i % 2 ==0 else np.round(128 + 1 * np.float(i)/n * 255)
    cv2.line(canvas, tuple(points[i]), (300, 700), color, int(round(1/n * 50 + 1)))
    cv2.line(canvas,(x, y+200), (x, y + 320), color, int(round(1/n * 50 + 1)))
#    print(x,y,z)
#cv2.imshow('ddd', canvas)
#cv2.waitKey()
cv2.imwrite('pie.jpg', canvas)
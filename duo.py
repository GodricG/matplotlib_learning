# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:45:44 2019

@author: Godric
"""

import numpy as np
import cv2
canvas = np.zeros((400, 600, 3), dtype = np.uint8) + 255
theta = np.pi / 5
rotations = np.array([
        [[np.cos(i * theta), -np.sin(i * theta)],
         [np.sin(i * theta), np.cos(i * theta)]
        ] for i in np.arange(1,10)
        ]).reshape(9,2,2)
#print(rotations)
points = []

a = np.array([[[[0, -1]] + [np.dot(m, (0, -1)) for m in rotations]]], dtype = np.float).reshape(10,2)
b = np.array([[[[0, -2]] + [np.dot(n, (0, -2)) for n in rotations]]], dtype = np.float).reshape(10,2)
#print(a, b)
for i in range(0,10):
    if i % 2 ==1:
        points.append(a[i])
    if i % 2 ==0:
        points.append(b[i])
points.append(b[9])
point = np.array([points[m] for m in range(10)], dtype = np.float)
#print(point)
polys = np.round(point * 40 + np.array([300, 200])).astype(np.int).reshape(1,10,2)
print(polys)
cv2.polylines(canvas, polys, True, (0, 255, 255),1)
cv2.imwrite('ddfasd.jpg', canvas)


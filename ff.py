# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:23:20 2019

@author: Godric
"""

import cv2
color_img = cv2.imread('ddd.jpg')
print(color_img.shape)
gray_img = cv2.imread('ddd.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)
cv2.imwrite('test_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('test_grayscale.jpg')
print(reload_grayscale.shape)
cv2.imwrite('test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))
cv2.imwrite('test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION,5))


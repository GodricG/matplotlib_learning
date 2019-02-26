# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:58:41 2019

@author: Godric
"""

import cv2
img = cv2.imread('test_imwrite.jpg')
img_200X200 = cv2.resize(img, (2000, 200))
img_300X200 = cv2.resize(img, (300, 200))
img_200X300 = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST)
img_300X300 = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value = (230, 180, 30))
patch = img[20:150, -180:-50]
#cv2.imwrite('1.jpg', patch)
#cv2.imwrite('resize200X200.jpg', img_200X200)
#cv2.imwrite('resize300X200.jpg', img_300X200)
#cv2.imwrite('resize_interpolation.jpg', img_interpolation)
#cv2.imwrite('resize_blackedge.jpg', img_blackedge)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
turn_green_hsv = img_hsv.copy()
turn_green_hsv[:, :, 0] = turn_green_hsv[:, :, 0] +100
print(img_hsv[0][0],turn_green_hsv[0][0])
turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
print(img[0][0],turn_green_img[0][0])
#cv2.imwrite('turn_green.jpg', turn_green_img)
colorless_hsv = img_hsv.copy()
colorless_hsv[:, :, 1] = (colorless_hsv[:, :, 1] * 0.1) % 256
colorless_img = cv2.cvtColor(colorless_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('colorless.jpg',colorless_img)
#darker_hsv = img_hsv.copy()
#darker_hsv[:, :, 2] = darker_hsv[:, :, 2] * 0.5
#darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
asd_hsv = img_hsv.copy()
asd_hsv[:,:,0] = asd_hsv[:, :, 0] + 15
asd_img = cv2.cvtColor(asd_hsv, cv2.COLOR_HSV2BGR)
#cv2.imwrite('darker.jpg', darker_img)
cv2.imwrite = ('asd.jpg', asd_img)
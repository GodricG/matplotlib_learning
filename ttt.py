# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:01:07 2019

@author: Godric
"""

import cv2
img = cv2.imread('test_imwrite.jpg')
imag = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imag_hsv = imag.copy()
#imag_hsv[:, :, 0] = (imag_hsv[:, :, 0] +55) 
for i in range(0,3,2):
    imag_hsv[:, :, i] = (imag_hsv[:, :, i] +15)
#print(imag[0][0], imag_hsv[0][0])
img_cvted = cv2.cvtColor(imag_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('test.jpg', img_cvted)

import numpy as np
hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
def gamma_trans(img, gamma):
    gamma_table = [np.power(x/255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
#    gamma_table = np.ones(256).reshape(1,256).astype(np.uint8)
#    gamma_table = gamma_table *100
    return cv2.LUT(img, gamma_table)
gamma_table = [np.power(x/255.0, 0.5) * 255.0 for x in range(256)]
gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
img_corrected = gamma_trans(img, 0.5)
print(img[0][1], img_corrected[0][1], gamma_table)
cv2.imwrite('faddsd.jpg', img_corrected)
hist_b_corrected = cv2.calcHist([img_corrected], [0], None, [256], [0, 256])
hist_g_corrected = cv2.calcHist([img_corrected], [1], None, [256], [0, 256])
hist_r_corrected = cv2.calcHist([img_corrected], [2], None, [256], [0, 256])
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
pix_hists = [
        [hist_b, hist_g, hist_r],
        [hist_b_corrected, hist_g_corrected, hist_r_corrected]
        ]
pix_vals = range(256)
for sub_plt, pix_hist in zip([121,122], pix_hists):
    ax = fig.add_subplot(sub_plt, projection = '3d')
    for c, z, channel_hist in zip(['b', 'g', 'r'], [20, 10, 0], pix_hist):
        cs = [c] * 256
        ax.bar(pix_vals, channel_hist, zs = z, zdir = 'y', color = cs, alpha = 0.618, edgecolor = 'none', lw = 0)
        ax.set_xlabel('Pixel Values')
        ax.set_xlim([0, 256])
        ax.set_ylabel('Counts')
        ax.set_zlabel('Channels')
plt.show()

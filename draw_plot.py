# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:28:18 2019

@author: Godric
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['ytick.major.size'] = 0            
np.random.seed(42)
x = np.linspace(0, 5, 100)
y = 2 * np.sin(x) + 0.3 * x ** 2
y_data = y + np.random.normal(scale = 0.3, size = 100)
plt.figure('data')
plt.plot(x, y_data, 'go--')
plt.figure('model')
plt.plot(x, y)
plt.figure('data & model')
plt.plot(x, y, 'k', lw = 3)
plt.scatter(x, y_data)
#plt.savefig('result.png')
speed_map = {
        'dog': (48, '#7199cf'),
        'cat': (45, '#4fc4aa'),
        'cheetah': (120, '#e1a7a2')
}
plt.figure('subplot')
a = plt.subplot(2,2,1)
a.set_title('sub_1')
plt.plot(x, y)
b = plt.subplot(222)
plt.plot(x,y_data)
c = plt.subplot(212)
c.set_title('test words')
plt.scatter(x, y_data)
plt.show()
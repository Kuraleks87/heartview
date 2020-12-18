# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:35:47 2020

@author: AKursanov
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(10,10))

img = cv2.imread('scene00001.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('scene00001_gs.jpg', img)


enges = cv2.Canny(img,5,50)
cv2.imwrite('scene00001_eng.jpg', enges)

plt.subplot(121),plt.imshow(img)
plt.subplot(121),plt.imshow(enges)

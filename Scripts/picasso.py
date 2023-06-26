# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:37:24 2023

@author: swami
"""

import math
import cv2
import random
import numpy as np

art = cv2.imread("C:/Users/swami/ARKPerceptionSwaminathanSK/ARK Task 2023/artwork_picasso.png", 0)
filt = cv2.imread("C:/Users/swami/ARKPerceptionSwaminathanSK/Scripts/filter.png", 0)

# filt = np.array([[255, 251], [94, 0]])

art2 = []
li = []



for i in range(art.shape[0]):
    li = []
    for j in range(art.shape[1]):
        li.append(art[i][j])
    art2.append(li)


for i in range(0, art.shape[0], 2):
    for j in range(0, art.shape[1], 2):
        x = i
        y = j
        if x < art.shape[0] and y < art.shape[1]:
            art2[x][y] = art[x][y] ^ filt[x-i][y-j]
        
        x = i+1
        y = j
        if x < art.shape[0] and y < art.shape[1]:
            art2[x][y] = art[x][y] ^ filt[x-i][y-j]
        
        x = i
        y = j+1
        if x < art.shape[0] and y < art.shape[1]:
            art2[x][y] = art[x][y] ^ filt[x-i][y-j]
            
        x = i+1
        y = j+1
        if x < art.shape[0] and y < art.shape[1]:
            art2[x][y] = art[x][y] ^ filt[x-i][y-j]

art2 = np.array(art2, dtype = np.uint8)
art2 = cv2.GaussianBlur(art2,(3,3),0)

cv2.imshow("art",art2)
cv2.imwrite("template.png", art2)
cv2.waitKey(0)
cv2.destroyAllWindows()
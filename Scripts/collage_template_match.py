# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 18:36:01 2023

@author: swami
"""

import math
import cv2
import random
import numpy as np

collage = cv2.imread("C:/Users/swami/ARKPerceptionSwaminathanSK/ARK Task 2023/collage.png", 0)
template = cv2.imread("C:/Users/swami/ARKPerceptionSwaminathanSK/Scripts/template.png", 0)

collage = cv2.GaussianBlur(collage, (3, 3), 0)

temp = np.array([])

sum_pairs = []

min_sum_pair = (-1, -1, -1)

min_sum = 255*255*100*100

for i in range(0, collage.shape[0], 100):
    for j in range(0, collage.shape[0], 100):
        temp = abs(collage[i:i+100, j:j+100] - template)
        temp = np.square(temp)
        sum_pairs.append((i, j, np.sum(temp)))

for x in sum_pairs:
    if x[2] < min_sum:
        min_sum = x[2]
        min_sum_pair = x

print(min_sum_pair)

# From here we get the abcissa and ordinate to be 100, 100.
# hence, password for the file would be int(200*pi) = 628

cv2.imshow("collage", collage)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()
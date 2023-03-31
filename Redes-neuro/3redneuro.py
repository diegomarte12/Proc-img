import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib import pyplot as plt
num = 0
guardar = str()
img = cv2.imread('matriz3.jpg',0)
#0.28 0.28 0,1       0.28 29.56 0,2
for i in range(0,280,28):
    ini_ver = i 
    fin_ver = i+27
    for j in range (0,280,28):
        ini_hor = j
        fin_hor = j+27
        num+=1
        guardar = str(num)+".jpg"

        img[ini_ver:fin_ver, ini_hor:fin_hor]
        #cv2.imwrite(guardar ,img[ini_ver:fin_ver, ini_hor:fin_hor])



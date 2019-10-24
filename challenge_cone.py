# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:49:41 2019

@author: bonda
"""

import numpy as np
import pandas as pd
from imageio import imread
from skimage.transform import resize
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

train = pd.read_csv('training.csv')
newid = [str(i) for i in train['Id']]

width, height = 512,512

file = os.listdir()

images = [imread('Images\Images\Training\\' + j) for j in newid]
resized = [resize(i, (width, height)) for i in images]
images = np.array(resized)

class_names = [0,1]
print(train[train['Category' == 0]])
#plt.figure()
#plt.imshow(images[0])
#plt.colorbar()
#plt.grid(False)
#plt.show()
#
#plt.figure(figsize=(10,10))
#for i in range(25):
#    plt.subplot(5,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(images[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[train[i]])
#plt.show()

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(16, (3, 3), strides = 1, activation='relu', input_shape=(100, 100, 3)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides = 2))
model.add(tf.keras.layers.Dropout(0.25))

model.compile(loss='binary_crossentropy',
 optimizer='rmsprop',
 metrics=['accuracy'])




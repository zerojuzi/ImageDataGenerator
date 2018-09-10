#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import packages

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import cv2
i=47
j=1
datagen = ImageDataGenerator(
        rotation_range=0.2,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
'''print('./data/'+str(j)+'.jpg')
img = cv2.imread('data/'+str(j)+'.jpg')
cv2.imshow('Image', img)
cv2.waitKey()
'''
for j in range(1,47):
    img = load_img('data/'+str(j)+'.jpg')
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)


    k = 0
    for batch in datagen.flow(x,
                              batch_size=1,
                              save_to_dir='data/',
                              save_prefix=str(j),
                              save_format='jpg'):
        k += 1
        if k > 20:
            break
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 01:09:46 2021

@author: Efe Kurdoğlu
"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from PIL import Image
from mss import mss

def onehot_labels(values):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    onehot_encoder = OneHotEncoder(sparse = False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded),1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    return onehot_encoded

def frames(id, key): # key is the buttons from the keyboard
    global i
    
    i += 1
    print("{}: {}".format(key, i)) # key: up, down, left, right arrow
    mon = {"top":385, "left":520, "width":250, "height":100}                                # i: for how many times we pressed the button
    img = mss().grab(mon) # get the ROC with the size of specified in mon
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./images/{}_{}_{}.png".format(key, id, i))
    
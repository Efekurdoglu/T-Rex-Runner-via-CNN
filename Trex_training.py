# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:53:37 2021

@author: Efe Kurdoğlu
"""

import glob
import os
import numpy as np
import seaborn as sns
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from func import onehot_labels

import warnings
warnings.filterwarnings("ignore")


images = glob.glob("./images/*.png")

width = 250
height = 100

X = []
Y = []

for image in images:
    
    filename = os.path.basename(image)
    label = filename.split("_")[0]
    img = np.array(Image.open(image).convert("L").resize((width, height)))
    img = img / 255
    X.append(img)
    Y.append(label)
    
X = np.array(X)
X = X.reshape(X.shape[0], width, height, 1)

# sns.countplot(Y)

Y = onehot_labels(Y)
train_X, test_X, train_y, test_y = train_test_split(X, Y , test_size = 0.25, random_state = 2)    

# cnn model
model = Sequential()   
model.add(Conv2D(32, kernel_size = (3,3), activation = "relu", input_shape = (width, height, 1)))
model.add(Conv2D(64, kernel_size = (3,3), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.4))
model.add(Dense(3, activation = "softmax"))

# if os.path.exists("./weights.h5"):
#     model.load_weights("weights.h5")
#     print("Weights loaded")    

model.compile(loss = "categorical_crossentropy", optimizer = "Adam", metrics = ["accuracy"])

model.fit(train_X, train_y, epochs = 35, batch_size = 64)

score_train = model.evaluate(train_X, train_y)
print("Training accuracy: %",score_train[1]*100)    
    
score_test = model.evaluate(test_X, test_y)
print("Test accuracy: %",score_test[1]*100)      
    
 
open("model.json","w").write(model.to_json())
model.save_weights("weights.h5")   
    
    




































































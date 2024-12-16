import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os
from matplotlib.pyplot import imshow
import random
from sklearn.utils.validation import validate_data
from sympy import shape
from sympy.tensor.array.arrayop import Faltten
from classification_model import load_directory
from test_cv2 import removeBackgroundFolder,singleRemoveBackground
from tensorflow.keras import Sequential,Input
from tensorflow.keras.layers import Dense,Conv2D,Dropout,MaxPool2D,Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
label_list,y_data,x_data = load_directory(r"d:\imgs")
print(y_data.shape)
print(x_data.shape)
print(len(label_list))
print(label_list[0])
# shuffle
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2,random_state=10,stratify=y_data)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
print(y_train[:10])
# image confirm
rlist = [ random.randint(0,len(x_train)) for i in range(10)]
print(rlist)
for ix,xnum in enumerate(rlist):
    plt.subplot(2,5,ix+1)
    plt.imshow(x_train[ix])
    plt.title(label_list[y_train[ix]])
    plt.xticks([])
    plt.yticks([])
plt.show()
# onehot encoding
y_train = tf.one_hot(y_train,10)
y_test = tf.one_hot(y_test,10)
model = Sequential()
model.add(Input(shape=(64,64,3)))
model.add(Conv2D(filters=64,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,3),padding="same"))
model.add(Dropout(0.2))
model.add(Conv2D(filters=128,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,3),padding="same"))
model.add(Dropout(0.2))
model.add(Conv2D(filters=256,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,3),padding="same"))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dropout(0.4))
model.add(Dense(256,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(64,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(32,activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(10,activation="softmax"))
model.summary()
model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["acc"])
cb = tf.keras.callbacks.EarlyStopping(
    monitor = 'val_acc',
    patience = 20,
    verbose = 1,
    mode = 'auto',
    restore_best_weights = True
)
fit_his = model.fit(x_train,y_train,epochs=100,validation_data=(x_test,y_test),callbacks=[cb],batch_size=100)
import pickle
with open("classification_image.history","wb") as fp:
    pickle.dump(fit_his,fp)
model.save("classification_image.keras")
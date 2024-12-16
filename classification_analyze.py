import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os
from matplotlib.pyplot import imshow
from sklearn.utils.validation import validate_data
from sympy import shape
from sympy.tensor.array.arrayop import Flatten
from classification_model import load_directory
from test_cv2 import removeBackgroundFolder,singleRemoveBackground
from tensorflow.keras import Sequential,Input
from tensorflow.keras.layers import Dense,Conv2D,Dropout,MaxPool2D,Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle
with open("classification_image.history","rb") as fp:
    fit_his = pickle.load(fp)
print(fit_his.history.keys())
plt.subplot(1,2,1)
plt.plot(fit_his.history["acc"],label="Train Acc")
plt.plot(fit_his.history["val_acc"],label="Valid Acc")
plt.legend()
plt.title("ACCURACY")
plt.subplot(1,2,2)
plt.plot(fit_his.history["loss"],label="Train Loss")
plt.plot(fit_his.history["val_loss"],label="Valid Loss")
plt.legend()
plt.title("LOSSES")
plt.show()
model = tf.keras.models.load_model("classification_image.keras")

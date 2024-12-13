import tensorflow as tf
import numpy as np
import matplotlib as plt
import cv2 as cv
from test_cv2 import removeBackgroundFolder,singleRemoveBackground



from tensorflow.keras import Sequential,Input
from tensorflow.keras.layers import Dense,Conv2D,Dropout,MaxPool2D
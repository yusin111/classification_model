import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os
from matplotlib.pyplot import imshow

from test_cv2 import removeBackgroundFolder,singleRemoveBackground
from tensorflow.keras import Sequential,Input
from tensorflow.keras.layers import Dense,Conv2D,Dropout,MaxPool2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
def imageArgument_sub(orimg): # 이미지 증강
    rn = np.random.randint(2,6)
    rn = round(rn/10,1)
    testimge1 = tf.image.random_brightness(orimg, rn)
    # testimge1=tf.image.random_crop(testimge1, size=(150,150,3))
    # testimge1 = tf.image.resize(testimge1,size=(256,256),method="nearest",preserve_aspect_ratio=True)


    # testimge1 = tf.image.random_flip_left_right(testimge1)
    # testimge1 = tf.image.random_flip_up_down(testimge1)
    pre_model=tf.keras.layers.RandomRotation((-0.2,0.3)) # 레이어 출력을 다시 정수로 변환
    testimge1 = pre_model(testimge1)
    pre_model=tf.keras.layers.RandomFlip(mode="HORIZONTAL_AND_VERTICAL")
    testimge1 = pre_model(testimge1)
    pre_model=tf.keras.layers.RandomZoom((-0.15,0.15),(-0.15,0.15))
    testimge1 = pre_model(testimge1)
    return np.array(testimge1).astype(np.uint8)
def readImageDirect(rpath):
    cnt = 0
    f_lists = os.listdir(rpath)
    for folder in f_lists:
        f_names = os.listdir(rpath + "\\" + folder)
        print(folder, ":", end="")
        for f_name in f_names:
            ori_img = cv.imread(rpath + "\\" + folder + "\\" + f_name)
            ori_img = cv.resize(ori_img, (256, 256))
            for ix in range(5):
                arg_img = imageAugment_sub(ori_img)
                cv.imwrite(rpath + "\\" + folder + "\\" + str(cnt)+f_name, arg_img)
                cnt+=1
            print(".", end="")
        print()
def load_directory(rootpath): # {label:[이미지 리스트]}
    f_lists = os.listdir(rootpath)
    print(f_lists)
    y_labels = []
    x_files = []
    for label,fpath in enumerate(f_lists):
        f_name = r"{}\{}".format(rootpath,fpath)
        f_names = os.listdir(f_name)
        # print(f_names)
        for p in f_names:
            y_labels.append(label)
            fimg = cv.imread(r"{}\{}".format(f_name,p))
            fimg = cv.cvtColor(fimg,cv.COLOR_BGR2RGB)
            fimg = cv.resize(fimg,(64,64))
            x_files.append(fimg)
    return f_lists,np.array(y_labels),np.array(x_files)


if __name__=="__main__":
    readImageDirect(r"D:\imgs") # 데이터 증강 호출

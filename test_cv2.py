import cv2 as cv
import numpy as np
from rembg import remove
import os
rpath = r"d:\imgs"
f_lists = os.listdir(rpath)

def removeBackgroundFolder(rpath):
    print(f_lists)
    for folder in f_lists:
        f_names = os.listdir(rpath+ "\\" +folder)
        print(folder,":",end="")
        for f_name in f_names:
            ori_img = cv.imread(rpath+ "\\" +folder + "\\" + f_name)
            ori_img = cv.resize(ori_img,(256,256))
            # cv.imshow("ori"+f_name,ori_img)
            rmbg_img = remove(ori_img)
            cv.imwrite(rpath+"\\"+folder+"\\"+f_name,rmbg_img)
            # cv.imshow(f_name,rmbg_img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            print(".",end="")
        print()
def singleRemoveBackground(imagePathName):
    ori_img = cv.imread(imagePathName)
    ori_img = cv.resize(ori_img,(256,256))


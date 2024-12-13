import cv2 as cv
import numpy as np
from rembg import remove
import os
#rpath=r"D:\imgs"
def removeBackgroundFolder(rpath):
   f_lists = os.listdir(rpath)
   #https://github.com/xuebinqin/U-2-Net
   #https://github.com/xuebinqin/DIS
   print(f_lists)
   for folder in f_lists:
       f_names = os.listdir(rpath+"\\"+folder)
       print(folder,":",end="")
       for f_name in f_names:
           ori_img = cv.imread(rpath+"\\"+folder+"\\"+f_name)
           ori_img = cv.resize(ori_img,(256,256))
           #cv.imshow("ori "+f_name,ori_img)
           rmbg_img = remove(ori_img)
           cv.imwrite(rpath+"\\"+folder+"\\"+f_name,rmbg_img)
           # cv.imshow(f_name,rmbg_img)
           # cv.waitKey(0)
           # cv.destroyAllWindows()
           print(".",end="")
       print()
def singleRemoveBackground(imagePathName):
   ori_img = cv.imread(imagePathName)
   ori_img = cv.resize(ori_img, (256, 256))
   # cv.imshow("ori "+f_name,ori_img)
   rmbg_img = remove(ori_img)
   cv.imwrite(imagePathName)
   print("배경이미지 제거가 완료 되었습니다.")
if __name__=="__main__":
   pass # 이파일을 직접 실행했을때 작동되는 코드
else:
   pass # 다른 파일에서 import 시 작동되는 코드
#grabCut
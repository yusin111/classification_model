import os
import cv2 as cv
rpath = r"d:\imgs"
list_dirs = os.listdir(rpath) # 디렉토리 목록
for directory in list_dirs:
    img_file_lists = os.listdir(rpath+"\\"+directory)
    for img in img_file_lists:
        # isdir 디렉토리 검사 , isfile 파일 검사
        if os.path.isfile(rpath+"\\"+directory+"\\"+img): # 파일검사
            img_mat = cv.imread(rpath+"\\"+directory+"\\"+img,cv.IMREAD_COLOR)
            img_mat = cv.resize(img_mat,[256,256],img_mat,interpolation=cv.INTER_AREA)
            cv.imshow(img+": delete is press d",img_mat)
            cv.moveWindow(img+": delete is press d",-256,0)
            key = cv.waitKey(0)
            # print(key)
            cv.destroyAllWindows() # enter 13 , 100 d
            if key==100: # d키 입력시 파일 삭제
                os.remove(rpath+"\\"+directory+"\\"+img)
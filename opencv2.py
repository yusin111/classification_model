import cv2
import cv2 as cv
import numpy as np

timg = cv.imread(r"d:\test.jpg",cv.IMREAD_COLOR)
timg = cv.resize(timg,[256,256])
gray_img = cv.cvtColor(timg,cv.COLOR_BGR2GRAY)
gray_img=cv.GaussianBlur(gray_img,(1,1),0)
cv.imshow("origin ",gray_img)
# contours = cv.Canny(gray_img.copy(),100,100)
# cv.imshow("origin ",contours)
g3adapt= cv.adaptiveThreshold(gray_img,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,5,2)
# retval,biimg= (cv.threshold(gray_img,130,255,cv.THRESH_BINARY_INV))
cv.imshow("binary ",g3adapt)

contours,hieracy = cv.findContours(
   g3adapt,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
testimg = cv.drawContours(timg.copy(), contours, -1, (255, 0, 0))
cv.imshow("test", testimg)


print(len(contours))# (576,2,1,2)
print(contours[4].shape)
print(contours[0][0][0][1])

xy_data=[]
for ix in range(256):
    xy_min = [300,300];xy_max=[0,0]
    for i,data in enumerate(contours):
       for n,indata in enumerate(data):
           #print(indata[0][1])#y  위치
           if indata[0][1]==ix:
               if xy_min[0]>indata[0][0]:
                   xy_min=indata[0]
               if xy_max[0]<indata[0][0]:
                   xy_max = indata[0]
    if xy_min[0]==300: # 추출이 안되고 있는곳 처리
        xy_min=[0,0]
    xy_data.append([xy_min,xy_max])
print(len(xy_data))
print(xy_data[0])
# 마스킹 레이어 안티엘리어싱
for ix in range(len(xy_data)):
    if ix+5>=256:
        break
    cur = xy_data[ix][0][0]
    cur1 = xy_data[ix+1][0][0]
    cur2 = xy_data[ix+2][0][0]
    cur3 = xy_data[ix+3][0][0]
    cur4 = xy_data[ix+4][0][0]
    cur5 = xy_data[ix+5][0][0]
    mean=(cur+cur1+cur2+cur3+cur4+cur5)/6
    summ=0;cntt=0
    if cur<mean:
        summ+=cur
        cntt+=1
    if cur1<mean:
        summ+=cur1
        cntt+=1
    if cur2<mean:
        summ+=cur2
        cntt+=1
    if cur3<mean:
        summ+=cur3
        cntt+=1
    if cur4<mean:
        summ+=cur4
        cntt+=1
    if cur5<mean:
        summ+=cur5
        cntt+=1
    if mean==0:break
    mean = summ//cntt
    if cur > mean:
        xy_data[ix][0][0]=mean

for ix in range(len(xy_data)):
    if ix+5>=256:
        break
    cur = xy_data[ix][1][0]
    cur1 = xy_data[ix+1][1][0]
    cur2 = xy_data[ix+2][1][0]
    cur3 = xy_data[ix+3][1][0]
    cur4 = xy_data[ix+4][1][0]
    cur5 = xy_data[ix+5][1][0]
    mean=(cur+cur1+cur2+cur3+cur4+cur5)/6
    summ=0;cntt=0
    if cur>mean:
        summ+=cur
        cntt+=1
    if cur1>mean:
        summ+=cur1
        cntt+=1
    if cur2>mean:
        summ+=cur2
        cntt+=1
    if cur3>mean:
        summ+=cur3
        cntt+=1
    if cur4>mean:
        summ+=cur4
        cntt+=1
    if cur5>mean:
        summ+=cur5
        cntt+=1
    mean = summ//cntt
    if cur < mean:
        xy_data[ix][1][0]=mean


# (576,2,1,2)
xy_data=np.array(xy_data)#(256,1,2,2)
xy_data= xy_data.reshape(256,1,2,2)
print(xy_data.shape)
extract_img = cv.drawContours(timg.copy(), xy_data, -1, (0, 0, 255))
cv.imshow("ext",extract_img)
print("=================")
cnt=0
new_img = np.zeros((timg.shape))+255
for ix,valarr in enumerate(timg): # ix = x 좌표
    for iy,val in enumerate(timg[ix]): # [[10 111][200 111]] iy = y 좌표
        if xy_data[ix,0,0,0] <= iy and xy_data[ix,0,1,0] >= iy and xy_data[ix,0,0,1] == ix:
            cnt+=1
            new_img[ix,iy]=timg[ix,iy]
new_img = new_img.astype(np.uint8)
cv.imshow("last_img",new_img)
xy_data_first = xy_data[:,0,0,:]
xy_data_second = xy_data[:,0,1,:]
pts = np.concatenate((xy_data_first,xy_data_second))

pts = pts.reshape((-1,2))
cv.polylines(timg,[pts],True,(0,255,255))
cv.imshow("a",timg)
# #면적순으로 컨투어 정렬
# sorted_contoure =sorted(contours,key=cv.contourArea,reverse=True)
# for i in range(len(sorted_contoure)):
#     contour = sorted_contoure[i]
#     epsilon = 0.01*cv.arcLength(contour,True)
#     approx = cv2.approxPolyDP(contour,epsilon,True)
#     cv.drawContours(timg, [contour], -1, (0, 0, 255))
#     cv.drawContours(timg, [approx], -1, (255, 0, 0))
# cv.imshow("gray", timg)

cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np

img = cv.imread('양계장_작음.PNG')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny=cv.Canny(img,200,400) ## Tlow=200, Thigh=400으로 
#캐니는 Thigh를 Tlow의 2~3배로 설정할 것을 권고

contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

Icontour=[]
for i in range(len(contour)):
    if contour[i].shape[0]>20:
        Icontour.append(contour[i])
        
cv.drawContours(img,Icontour,-1,(255,0,0),1)

cv.imshow('Original with contours', img)
cv.imshow('Canny', canny)

cv.waitKey()
cv.destroyAllWindows()
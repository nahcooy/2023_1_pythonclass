import cv2 as cv
import sys

chicken=cv.imread('양계장1.PNG') 

if chicken is None:
    sys.exit('파일을 찾을 수 없습니다.')

graychicken=cv.cvtColor(chicken,cv.COLOR_BGR2GRAY)
smallgraychicken=cv.resize(graychicken,dsize=(0,0),fx=0.7,fy=0.7)

cv.imwrite('양계장1_흑백.PNG',graychicken)
cv.imwrite('양계장1_흑백_작음.PNG',smallgraychicken) 

cv.imshow('Color image',chicken)
cv.imshow('Gray image',graychicken)
cv.imshow('Gray image small',smallgraychicken)

cv.waitKey()
cv.destroyAllWindows()
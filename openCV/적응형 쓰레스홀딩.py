import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

block_size = 91 #블럭 사이즈
C = 5 #차감 상수
img_0 = cv.imread('양계장_작음.PNG', cv.IMREAD_GRAYSCALE) #그래이 스케일로 읽기
img = cv.resize(img_0, (0,0), fx=0.7, fy=0.7)

#오츠 알고리즘으로 단일 경계값을 전체 이미지에 적용
ret, th1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,block_size, C)

th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,block_size, C)

#Matplot으로 결과 출력
imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, 'Adaptived-Mean': th2, 'Adapted-Gaussian': th3}

cv.imshow('Original', img)
cv.imshow('Global-Otsu', th1)
cv.imshow('Adaptived-Mean', th2)
cv.imshow('Adapted-Gaussian', th3)


cv.waitKey()
cv.destroyAllWindows()

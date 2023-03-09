import cv2 as cv
import numpy as np

chi_img=cv.imread('양계장_작음.PNG')
patch=chi_img[50:200,150:300,:]


patch1=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_NEAREST)
patch2=cv.resize(patch, dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_LINEAR)
patch3=cv.resize(patch, dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_CUBIC)

cv.imshow('Original',cv.resize(patch, (0,0),fx=5,fy=5))
cv.imshow('Resize nearest',patch1) #최근접 이웃
cv.imshow('Resize bilinear',patch2) #양선형

cv.waitKey()
cv.destroyAllWindows() 
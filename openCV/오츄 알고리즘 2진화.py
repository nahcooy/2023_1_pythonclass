import cv2 as cv
import sys

img=cv.imread('KakaoTalk_20230215_202139669.jpg')
resized_img = cv.resize(img, (0,0), fx=0.5, fy=0.5)

cv.imshow('R channel',resized_img[:,:,2])
cv.imshow('G channel',resized_img[:,:,1])
cv.imshow('B channel',resized_img[:,:,0])

#threshold(채널 2진화,명암값의 범위,threshold알고리즘(오츄))
t_r,r_bin_img=cv.threshold(resized_img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
t_g,g_bin_img=cv.threshold(resized_img[:,:,1],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
t_b,b_bin_img=cv.threshold(resized_img[:,:,0],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow('R channel binarization',r_bin_img) #채널 이진화
cv.imshow('G channel binarization',g_bin_img)
cv.imshow('B channel binarization',b_bin_img)

print('오츄 최적 임계값 = R: {0} G: {1} B={2}'.format(t_r, t_g, t_b))

cv.waitKey()
cv.destroyAllWindows() 

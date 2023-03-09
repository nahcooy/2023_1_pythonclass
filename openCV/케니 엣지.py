#Canny - 에지 검출에서는 가우시언에 1차 미분을 적용한 연산자가 최적이라는 사실을 수학적으로 증명
import cv2 as cv

img = cv.imread('가나다라.jpg', cv.IMREAD_GRAYSCALE)

canny1=cv.Canny(img,50,150) # Tlow=50, Thigh=150으로 설정
canny2=cv.Canny(img,200,400) ## Tlow=200, Thigh=400으로 
#캐니는 Thigh를 Tlow의 2~3배로 설정할 것을 권고

cv.imshow('Original', img)
cv.imshow('Canny1', canny1)
cv.imshow('Canny2', canny2)

cv.waitKey()
cv.destroyAllWindows()
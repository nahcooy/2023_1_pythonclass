import cv2 as cv
import sys

img = cv.imread('양계장1.PNG')

if img is None:
    sys.exit('파일 없음')
else:
    print("파일 있음")

small_img=cv.resize(img, (0,0), fx=0.3,fy=0.3) 

cv.imwrite('양계장_작음.PNG', img) # 영상을 파일에 저장
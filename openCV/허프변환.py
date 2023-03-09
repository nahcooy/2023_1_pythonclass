import cv2 as cv

img=cv.imread('양계장_작음.PNG')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

chicken = cv.HoughCircles(gray, cv.HOUGH_GRADIENT,1,5,param1=50,param2=20,minRadius=5,maxRadius=15)

for i in chicken[0]:
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)
    
cv.imshow('chicken detection', img)

cv.waitKey()
cv.destroyAllWindows()


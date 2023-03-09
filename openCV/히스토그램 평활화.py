import cv2 as cv
import matplotlib.pyplot as plt

chi_img=cv.imread('양계장_작음.PNG') 

chi_gray=cv.cvtColor(chi_img,cv.COLOR_BGR2GRAY)
#흑백영상으로 바꾸기

plt.imshow(chi_gray,cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()
#확실히 흑백영상으로 바꾸기

h=cv.calcHist([chi_gray],[0],None,[256],[0,256]) # 히스토그램 구하여 출력
plt.plot(h,color='r',linewidth=1), plt.show()

equal=cv.equalizeHist(chi_gray) # 히스토그램 평활화하고 출력
plt.imshow(equal,cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

h=cv.calcHist([equal],[0],None,[256],[0,256]) # 히스토그램 구하여 출력
plt.plot(h,color='r',linewidth=1), plt.show()



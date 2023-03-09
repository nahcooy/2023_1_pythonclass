import cv2 as cv
#명암이 서서히 변하는게 물체의 경계는 명암이 급격히 변할 가능성이 높다
#𝑓(X)^-1 = 𝑓(𝑥 + 1)− 𝑓(𝑥)
chi_img=cv.imread('양계장_작음.PNG')
gray_chi = cv.cvtColor(cv.resize(chi_img,(0,0),fx=0.5,fy=0.5),cv.COLOR_BGR2GRAY) #영상을 흑백으로 변환

#Sobel(영상, 결과영상 데이터 타입, x방향 미분차수, y방향 미분차수, 커널크기(대체로3), 영상에 곱할값(대체로 1), 영상에 더할값(대체로 1))
grad_x=cv.Sobel(gray_chi,cv.CV_32F,1,0,ksize=3) # 소벨필터로 엣지 찾기
grad_y=cv.Sobel(gray_chi,cv.CV_32F,0,1,ksize=3)

sobel_x=cv.convertScaleAbs(grad_x) # 절대값으로 변환
sobel_y=cv.convertScaleAbs(grad_y)

edge_strength=cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0) # 에지 강도 계산
#x와y를 0.5씩 곱해서 더한다

cv.imshow('Original',gray_chi) 
cv.imshow('sobelx',sobel_x)  #수직 방향의 엣지가 선명
cv.imshow('sobely',sobel_y)  #수평 방향의 엣지가 선명
cv.imshow('edge strength',edge_strength) 

cv.waitKey()
cv.destroyAllWindows() 
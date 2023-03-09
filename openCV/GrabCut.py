import cv2 as cv
import numpy as np

img=cv.imread('양계장_작음.PNG')
img_show=np.copy(img) #그림 그릴 영상 복사

mask=np.zeros((img.shape[0],img.shape[1]), np.uint8)
#img의 크기와 같은 검정 영상 만들기
mask[:,:]=cv.GC_PR_BGD
#mask를 배경으로 초기화 GC_PR_BGD = (확신하는 백그라운드, 백그라운드로 생각되는 것)

BrushSiz=4 #붓의 크기
LColor,RColor=(255,0,0),(0,0,255) #(B,G,R)

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN: #왼버튼 누르기
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1) 
        #circle(영상, 중심좌표, 반지름, 색상, 선두께(-1이면 안쪽을 채움), 선타입, 그리기 좌표 값의 축소 비율(기본값=0))
        #작은 원을 연속적으로 그려서 붓과 같은 효과를 낸다
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)
    elif event==cv.EVENT_RBUTTONDOWN: #오른버튼 누르기
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON: #왼버튼 누르고 이동하기
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON: #오른버튼 누르고 이동하기
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)
        #누르고 이동하기만 있어도 되지 않을까?
        
    cv.imshow('chi_painting',img_show)
        
cv.namedWindow('chi_painting')
cv.setMouseCallback('chi_painting', painting)

while(True):
    if cv.waitKey(1)==ord('q'):
        break

background=np.zeros((1,65),np.float64)
foreground=np.zeros((1,65),np.float64)

cv.grabCut(img,mask,None,background,foreground,5,cv.GC_INIT_WITH_MASK)
mask2=np.where((mask==cv.GC_BGD)|(mask==cv.GC_PR_BGD),0,1).astype('uint8')
grab=img*mask2[:,:,np.newaxis]

cv.imshow('Grab cut image', grab)

cv.waitKey()
cv.destroyAllWindows()


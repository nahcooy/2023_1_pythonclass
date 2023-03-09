import cv2 as cv

chi_cp = cv.VideoCapture("닭1.mp4")

'''width = chi_cp.get(cv.CAP_PROP_FRAME_WIDTH)
height = chi_cp.get(cv.CAP_PROP_FRAME_HEIGHT)
print('original size: %d, %d' % (width, height))

chi_cp.set(cv.CAP_PROP_FRAME_WIDTH, 100)
chi_cp.set(cv.CAP_PROP_FRAME_HEIGHT, 80)

width = chi_cp.get(cv.CAP_PROP_FRAME_WIDTH)
height = chi_cp.get(cv.CAP_PROP_FRAME_HEIGHT)
print('changed  size: %d, %d' % (width, height))
'''
while True:
    ret,frame=chi_cp.read()
    resize = cv.resize(frame, (0,0), fx=0.3, fy=0.3)
    if not ret:
        print('프레임 획득 실패')
        break
    cv.imshow('Video display', frame)
    cv.imshow('resized Video display',resize)
    
    key=cv.waitKey(1)
    if key==ord('q'):
        break

chi_cp.release()
cv.destroyAllWindows()
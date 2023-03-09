import cv2 as cv

chi_cp = cv.VideoCapture("닭1.mp4")

while True:
    ret,frame=chi_cp.read()
    if not ret:
        print('프레임 획득 실패')
        break

    cv.imshow('Video display',frame)

    key=cv.waitKey(1)
    if key==ord('q'):
        break

chi_cp.release()
cv.destroyAllWindows()
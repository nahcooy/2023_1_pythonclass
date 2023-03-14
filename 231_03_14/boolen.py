#과제 #03 - 6) 두 지점 사이 거리 구하기
import math

while True:
    x1 = int(input("x1의 값을 입력해주세요: "))
    y1 = int(input("y1의 값을 입력해주세요: "))
    x2 = int(input("x2의 값을 입력해주세요: "))
    y2 = int(input("y2의 값을 입력해주세요: "))
    #x1, y1, x2, y2 = map(int, input().split())

    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    if distance <= 1:
        print("두점 사이의 거리가 너무 가깝습니다. 좌표를 다시 입력해주세요.")
    else:
        break


print("두 지점 사이의 거리: {}".format(round(distance, 2)))
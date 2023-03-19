#과제 #04 - 2) 과제#03를 수정하여, x, y를 입력받아서, 어느 사분면인지 출력하시오.
import math

x = int(input("x좌표의 값을 입력해주세요: "))
y = int(input("y좌표의 값을 입력해주세요: "))

#x, y = map(int, input("x와 y좌표를 순서대로 입력해주세요").split())

if x == 0 or y ==0:
    if x == 0:
        if y != 0:
            print("입력한 좌표는 y축 위에 있습니다.")
            exit()
        else:
            print("입력한 좌표는 (0, 0)입니다")
            exit()
    else:
        print("입력한 좌표는 x축 위에 있습니다")
        exit()

if x > 0:
    if y > 0:
        print("입력한 좌표는 1사분면입니다.")
    else:
        print("입력한 좌표는 4사분면입니다.")

else:
    if y > 0:
        print("입력한 좌표는 3사분면입니다.")
    else:
        print("입력한 좌표는 2사분면입니다.")
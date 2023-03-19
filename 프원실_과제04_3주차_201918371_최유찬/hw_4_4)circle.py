#과제 #04 - 3)과제#03에서 반지름을 입력받아서, 원의 둘레와 원의 면적을 출력하는 프로그램을 작성하시오
import math

r = int(input("원의 반지름을 입력하세요 -> ")) #반지름
pi = math.pi #math 라이브러리에서 pi값 가져오기
c = 2*r*pi #원의 둘레
s = math.pow(r, 2)*pi #원의 넓이 math 라이브러리에서 pow 사용

print("The circumference of the circle is {:.1f}\nThe area of the circle is {:.2f}".format(c, s)) #format으로 소수점 정리

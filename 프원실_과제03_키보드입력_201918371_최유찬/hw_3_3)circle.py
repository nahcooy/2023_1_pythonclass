#과제 #03 - 3)과제02-3 수정하기(input 이용, math 이용)
import math

r = int(input()) #반지름
pi = math.pi #math 라이브러리에서 pi값 가져오기
s = math.pow(r, 2)*pi #math 라이브러리에서 pow 사용

print("The area of the triangle is {}".format(round(s, 2))) #round함수로 소수점 2자리에서 반올림

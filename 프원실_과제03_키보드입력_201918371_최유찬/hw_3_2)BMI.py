#과제 #03 실습02/실습03 완성하기 – BMI를 구하기 (input 이용, math 이용)
import math

print("Calculate BMI\nEnter your weight and height")
w, h = map(float, input().split())

print("Your weight is {}kg and your height is {}cm".format(w, h))
#BMI = w/((h/100)**2)
BMI = w/math.pow((h/100), 2) #pow로 제곱연산 수행

print("Your BMI is {}".format(round(BMI, 2)))

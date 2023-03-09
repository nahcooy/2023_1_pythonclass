#과제 #02 - 간단한연산 중 2번 키와 몸무게가 임의로 주어졌을 때 BMI 구하기
print("Calculate BMI\nEnter your weight and height")
#w, h = map(float, input().split())

w = 60
h = 170
print("Your weight is {}kg and your height is {}cm".format(w, h))
BMI = w/((h/100)**2)

print("Your BMI is {:.2f}".format(BMI))

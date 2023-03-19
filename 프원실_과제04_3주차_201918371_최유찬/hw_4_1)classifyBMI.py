#과제 #04 - 1) 과제#03의 BMI 계산결과에 따라 아래 텍스트를 참고하여, 비만 정도를 표시하시오.
import math

print("Calculate BMI\nEnter your weight and height")
w, h = map(float, input().split())

print("Your weight is {}kg and your height is {}cm".format(w, h))
#BMI = w/((h/100)**2)
BMI = w/math.pow((h/100), 2) #pow로 제곱연산 수행

print("Your BMI is {}".format(round(BMI, 2)))

if BMI>=35:
    print("According to your BMI, you are 'level 3 obese'")
elif BMI>=30:
    print("According to your BMI, you are 'level 2 obese'")
elif BMI >= 25:
    print("According to your BMI, you are 'level 1 obese'")
elif BMI >= 23:
    print("According to your BMI, you are 'pre-obese'")
else:
    print("According to your BMI, you are 'normal'")


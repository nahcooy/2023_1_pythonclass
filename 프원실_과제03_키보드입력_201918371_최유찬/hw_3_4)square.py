#과제 #03 - 4) 과제02-4 수정하기(input 3번 입력받기)

#underside, upperside, height = map(float, input().split())
underside = float(input())
upperside = float(input())
height = float(input())

s = (underside+upperside)*height/2

print("The area of the rectangle is {}".format(round(s, 2)))
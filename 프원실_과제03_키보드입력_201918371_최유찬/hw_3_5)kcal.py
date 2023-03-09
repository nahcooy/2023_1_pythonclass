#과제 #03 - 5) 칼로리 구하기 (과일마다 섭취 g를 입력받아서 칼로리 출력하기)

halabong = int(input("섭취한 한라봉의 무게(g): "))
strawberry = int(input("섭취한 딸기의 무게(g): "))
banana = int(input("섭취한 바나나의 무게(g): "))
#input함수 3개를 통해 섭취한 과일의 무게를 정수형으로 각각 받습니다
h_kcal = 0.5
s_kcal = 0.34
b_kcal = 0.77

totalkcal = halabong*h_kcal + strawberry*s_kcal + banana*b_kcal

print("섭취한 총 칼로리는 {}kcal입니다".format(round(totalkcal, 2)))
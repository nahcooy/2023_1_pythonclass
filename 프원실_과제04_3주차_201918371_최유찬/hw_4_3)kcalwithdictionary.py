#과제 #04 - 3) 과제#03에서 칼로리 계산 프로그램을 사전형(딕셔너리)를 이용하여 구현하시오.

halabong = int(input("섭취한 한라봉의 무게(g): "))
strawberry = int(input("섭취한 딸기의 무게(g): "))
banana = int(input("섭취한 바나나의 무게(g): "))
#input함수 3개를 통해 섭취한 과일의 무게를 정수형으로 각각 받습니다

fruit_calories = {
    "h_kcal": 0.5,
    "s_kcal": 0.34,
    "b_kcal": 0.77
}
#과일별 칼로리를 딕셔너리로 만듭니다.



totalkcal = halabong*fruit_calories["h_kcal"] + strawberry*fruit_calories["s_kcal"] + banana*fruit_calories["b_kcal"]

print("섭취한 총 칼로리는 {}kcal입니다".format(round(totalkcal, 2)))
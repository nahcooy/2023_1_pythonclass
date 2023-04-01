#과제 #07 -  4) fruits={“딸기”: 300, “한라봉”: 150} 과 같이, 딸기 300g, 한라봉 150g 섭취하였을 때, 총 칼로리를 계산하시오. 과제 #04 활용

def fruits_eaten(fruits):
    for k, v in fruits.items():
        print("당신이 섭취한 {}는 {}g입니다".format(k, v))
    return None


def kcal_calculator(fruits, fruits_kcal):
    total_kcal = 0
    for k, v in fruits.items():
        total_kcal += v*fruits_kcal[k]
    print("당신이 섭취한 총 칼로리는 {:.1f}kcal입니다".format(total_kcal))

def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruit_kcal = {"딸기": 0.34, "한라봉": 0.5}
    fruits_eaten(fruits)
    kcal_calculator(fruits, fruit_kcal)

if __name__ == "__main__":
	main()
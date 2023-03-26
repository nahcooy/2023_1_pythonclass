#과제 #06 -  4) fruits={“딸기”: 300, “한라봉”: 150} 과 같이, 딸기 300g, 한라봉 150g 섭취하였을 때, 총 칼로리를 계산하시오. 과제 #04 활용


def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruit_calories = {"h_kcal": 0.5, "s_kcal": 0.34}
    total_kcal = fruits["딸기"]*fruit_calories["s_kcal"]+fruits["한라봉"]*fruit_calories["h_kcal"]
    print("당신이 섭취한 딸기는 {}g, 한라봉은 {}g입니다\n당신이 섭취한 총 칼로리는 {:.1f}kcal입니다".format(fruits["딸기"], fruits["한라봉"], total_kcal))

if __name__ == "__main__":
	main()
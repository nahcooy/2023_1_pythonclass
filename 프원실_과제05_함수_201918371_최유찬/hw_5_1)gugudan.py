#과제 #05 - 1)숫자를 입력받아, 해당하는 구구단을 출력하는 함수 gugudan(dan)를 만드시오.
def gugudan(x):
    if x >= 1 and x<=9:
        print("구구단 {}단을 출력합니다".format(x))
        for i in range(9):
            print("{} * {} = {:2d}".format(x, i+1, x*(i+1)))
    else:
        x = int(input("'1~9'사이의 숫자를 다시 입력해주세요 -> "))
        gugudan(x)
def main():
    dan = int(input("구구단 출력기입니다. 1~9사이의 숫자를 입력해주세요 -> "))
    gugudan(dan)

if __name__ == "__main__":
	main()
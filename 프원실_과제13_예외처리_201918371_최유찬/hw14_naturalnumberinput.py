import sys

def main():
    print("리스트로 만들고 싶은 자연수들을 엔터로 구분하여 입력해주세요\n -1을 입력하면 입력이 종료되고, 리스트가 출력됩니다")
    numlist = list()

    while True:
        y = sys.stdin.readline().strip()
        try:
            x = int(y)
        except ValueError:
            print(f"{y}는 자연수가 아닙니다")
            pass
        else:
            if x == -1:
                print("숫자리스트를 출력하고, 프로그램을 종료합니다")
                print(numlist)
                return
            if x <= 0:
                print(f"{x}는 자연수가 아닙니다")
            else:
                numlist.append(x)
if __name__ == "__main__":
    main()

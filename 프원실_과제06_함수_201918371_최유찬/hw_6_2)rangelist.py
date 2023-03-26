#과제 #06 - 2)1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 range_list(n)

def range_list(n):
    a = list()
    for i in range(n):
        a.append(i+1)
    return a
def main():
    number = int(input("1~n까지 리스트를 만들 n을 입력해주세요\n"))
    print("1~n까지 리스트 출력합니다\n{}".format(range_list(number)))
if __name__ == "__main__":
	main()
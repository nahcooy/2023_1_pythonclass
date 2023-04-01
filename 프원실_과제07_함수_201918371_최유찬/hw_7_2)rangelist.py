#과제 #07 - 2)1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 range_list(n)

def range_list1(n): #for문과 append함수를 이용한 list만들기
    results = list()
    for i in range(n):
        results.append(i+1)
    return results

def range_list2(n): #range함수를 이용하여 list를 만든다
    return list(range_list1((1, n+1))) #range(1, n+1) -> 1~n

def main():
    number = int(input("1~n까지 리스트를 만들 n을 입력해주세요\n"))
    print("1~n까지 리스트 출력합니다\n{}".format(range_list1(number)))
if __name__ == "__main__":
	main()
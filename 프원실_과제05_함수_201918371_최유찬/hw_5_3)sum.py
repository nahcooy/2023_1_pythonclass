#과제 #05 - 3)숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하시오. 함수명은 sum_n(n)
def sum_n(n):
    sum = 0
    for i in range(n):
        sum += i+1
    print("1부터 {}까지의 합은: {}입니다".format(n, sum))

def main():
    n = int(input("1부터 n까지의 합을 구할 n을 입력해주세요 -> "))
    sum_n(n)
if __name__ == "__main__":
	main()
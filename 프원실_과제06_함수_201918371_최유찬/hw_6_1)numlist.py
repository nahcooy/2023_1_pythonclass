#과제 #06 - 1)숫자 리스트를 매개변수로 받아서 평균을 구하시오. 함수는 average(nums)

def average(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)
def main():
    n = list(map(int, input("평균을 구한 숫자들을 띄어쓰기로 구분하여 입력하시오\n").split()))
    print("입력한 수들의 평균은 {:.2f}입니다".format(average(n)))
if __name__ == "__main__":
	main()
#과제 #07 - 1)숫자 리스트를 매개변수로 받아서 평균을 구하시오. 함수는 average(nums)
import statistics

def average1(nums): #sum과 len함수를 이용한 평균 구하기
    if len(nums)>0:
        return sum(nums)/len(nums)
    return None

def average2(nums): #for문을 이용하여 sum을 구하고 len함수를 이용한 평균 구하기
    if not len(nums):
        return None
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)

def average3(nums): #for문을 이용하여 sum과 len을 구하여 평균 구하기
    list_sum = 0
    list_count = 0
    for num in nums:
        list_sum += num
        list_count += 1
    if list_count > 0:
        return list_sum/list_count
    return None

def average4(nums): #statistics.mean(list)을 이용한 평균 구하기
    return statistics.mean(nums)

def main():
    n = list(map(int, input("평균을 구한 숫자들을 띄어쓰기로 구분하여 입력하시오\n").split()))
    print("입력한 수들의 평균은 {:.2f}입니다".format(average1(n)))

if __name__ == "__main__":
	main()
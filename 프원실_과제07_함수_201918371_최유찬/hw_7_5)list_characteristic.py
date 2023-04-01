#과제 #07 -  5)split으로 문자열 리스트로 만들고, 평균값, 중앙값, 최솟값, 최댓값 구하기
def text2list(text):
    return list(map(int, text.split()))

def average(num_list):
    if len(num_list) > 0:
        return sum(num_list) / len(num_list)
    return None

def median(num_list):
    sorted_num_list = sorted(num_list)
    return sorted_num_list[len(sorted_num_list)//2]

def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    # # 단, 갯수가 짝수일때는 중앙에 위치한 두 값 중 큰 값을 채택한다.
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

if __name__ == "__main__":
    main()
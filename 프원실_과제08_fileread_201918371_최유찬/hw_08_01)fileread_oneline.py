def read_textfile_words_in_line(filename):
    with open(filename, "r") as f:
        return list(map(int, f.read().split())) #split을 사용하여 띄어쓰기로 나누어진 문자들을 받고, map을 사용해서 int로 바꾸어준다.

def average(num_list):
    if len(num_list) > 0:
        return sum(num_list) / len(num_list)
    return None

def median(num_list):
    sorted_num_list = sorted(num_list)
    return sorted_num_list[len(sorted_num_list)//2]

def main():
    filename = "several_words_in_one_line.txt"
    nums = read_textfile_words_in_line(filename)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    # # 단, 갯수가 짝수일때는 중앙에 위치한 두 값 중 큰 값을 채택한다.
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

if __name__ == "__main__":
    main()
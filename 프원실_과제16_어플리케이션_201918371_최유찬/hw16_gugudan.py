import random
import hw16_gui_input_code

def gugudan_test(num_list_for_gugudan, question_num, testcase):
    x, y = map(int, random.choice(num_list_for_gugudan))
    user_answer = int(hw16_gui_input_code.gui_input(f"{x} * {y}의 결과를 입력하시오"))
    correct_answer = x * y

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print(f"{question_num}번 문제")
    if user_answer == correct_answer:
        print("정답입니다")
    else:
        print("오답입니다")
        print(f"{x} * {y} = {correct_answer}입니다")

    # 시간복잡도를 조금이라도 줄이기 위해, 마지막 문제에 대한 답변 출력이 완료되면, for문을 break한다
    if question_num == testcase:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return

    # 앞선 문제와 같은 문제를 다시 내는 것을 방지하기 위해 num_list_for_gugudan에서 앞선 문제를 remove한다
    if x == y:
        num_list_for_gugudan.remove([x, y])
    else:
        num_list_for_gugudan.remove([x, y])
        num_list_for_gugudan.remove([y, x])

def main():
    testcase = int(hw16_gui_input_code.gui_input("구구단 문제의 개수를 1~10사이의 자연수로 입력해주세요\ndefault값은 5입니다"))

    #testcase의 default값은 5이다
    #만약 1~10사이의 숫자가 아닌 다른 숫자가 입력된다면, testcase를 default값인 5로 초기화한다
    if testcase < 1 or testcase > 9:
        testcase = 5

    #testcase간 중복 문제를 최소화하기 위하여 random.randint대신 random.choice를 사용하였음을 알려드립니다
    num_list_for_gugudan = list()
    for i in range(1, 10):
        for j in range(1, 10):
            num_list_for_gugudan.append([i, j])

    #for문 안의 계산을 줄이기 위해 range를 1부터로 설정한다
    for question_num in range(1, testcase+1):
        #구구단 함수를 시행합니다
        gugudan_test(num_list_for_gugudan, question_num, testcase)

    #for문이 종료되면 프로그램이 종료된다
    print("\n프로그램이 종료됩니다")
    return
if __name__=="__main__":
    main()
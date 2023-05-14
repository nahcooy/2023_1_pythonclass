import random
import hw16_gui_input_code

def hangman_game(hangman_word, user_game_mode):
    #단어 길이에 따라 trial값을 조정한다
    if len(hangman_word) < 5:
        trial = 10
    else:
        trial = len(hangman_word)+6

    # 난이도에 따라 trial값을 조정한다
    if user_game_mode == 1:
        trial += 3
    elif user_game_mode == 3:
        trial -= 3

    user_trial = 0
    user_answer_list = ["_"] * len(hangman_word)
    user_input_list = [False] * 26

    # 사용자가 trial 이내에 정답을 맞출 때까지 반복한다
    while user_trial < trial and "".join(user_answer_list) != hangman_word:
        user_answer = " ".join(user_answer_list)
        # 사용자로부터 알파벳 한 문자를 입력받는다
        user_input = hw16_gui_input_code.gui_input(f"{user_answer} (trial={trial - user_trial})\n 알파벳 한 문자를 입력하시오 => ")

        # 사용자 입력값이 알파벳이 아닐 경우
        if not (65 <= ord(user_input) <= 90 or 97 <= ord(user_input) <= 122):
            print("잘못된 입력입니다. 알파벳 한 문자를 입력해주세요.")
            continue
        # 사용자 입력값이 대문자인 경우, 소문자로 변환한다
        elif ord(user_input) <= 90:
            user_input = chr(ord(user_input) + 32)

        # 사용자 입력값이 이미 입력된 값일 경우
        if not user_input_list[ord(user_input) - 97]:
            user_input_list[ord(user_input) - 97] = True
        else:
            print("이미 입력된 문자입니다")
            continue

        # 사용자 입력값이 정답 단어에 포함될 경우
        if user_input in hangman_word:
            for i in range(len(hangman_word)):
                if hangman_word[i] == user_input:
                    user_answer_list[i] = user_input
            print(" ".join(user_answer_list))
            print("정답입니다!")
        # 사용자 입력값이 정답 단어에 포함되지 않을 경우
        else:
            user_trial += 1
            print(f"입력문자 {user_input}, 틀렸습니다.")

    # 사용자가 정답을 맞췄을 경우
    if "".join(user_answer_list) == hangman_word:
        print("축하합니다! 정답을 맞추셨습니다.")
    # 사용자가 모든 기회를 소진했을 경우
    else:
        print("기회를 모두 소진하셨습니다. 정답은 {}입니다.".format(hangman_word))

def main():
    #문제를 낼 영어단어 목록입니다
    #max_len = 9, min_len = 3이다
    words_list = ['apple', 'banana', 'orange', 'peach', 'grape', 'tiger', 'elephant', 'giraffe', 'lion', 'zebra', 'red',
             'green', 'blue', 'yellow', 'purple', 'black', 'white', 'chemistry', 'biology', 'physics', 'astronomy',
             'teacher', 'doctor', 'engineer', 'pilot']

    user_game_mode = int(hw16_gui_input_code.gui_input("hangman 게임의 난이도를 설정해주세요\n난이도는 easy, normal, hard 3가지로 나누어져있습니다\n1을 입력하면 easy, 2를 입력하면 normal, 3을 입력하면 hard입니다\ndefault 난이도는 normal입니다"))

    #user_game_mode가 1,2,3이 모두 아닐 경우 default값인 2로 초기화한다
    if user_game_mode not in [1, 2, 3]:
        user_game_mode = 2

    #random.choice로 words_list의 단어 중 하나를 선택한다
    hangman_word = random.choice(words_list)
    #선택한 단어를 매개변수로 hangman_game함수를 실행한다.
    hangman_game(hangman_word, user_game_mode)

    print("\n프로그램이 종료됩니다")
    return

if __name__=="__main__":
    main()
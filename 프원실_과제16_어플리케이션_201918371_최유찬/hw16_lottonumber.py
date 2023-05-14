import random
import hw16_gui_input_code

def mk_lotto_numberlist():
    #random.sample을 사용하여 1~45의 숫자 중에서 6개를 중복없이 '한번에' 추출
    return random.sample(range(1, 46), 6)

def lotto_generator(num_of_lotto_draws):
    #중복 검사를 고려하여 lotto_numbers라는 list만들기
    lotto_numbers = []
    for _ in range(num_of_lotto_draws):
        while True:
            lotto_number = mk_lotto_numberlist()
            #아무래도 추첨번호가 겹치지 않게 하는 것이 좋을 것 같아서 if문을 추가하였습니다
            if lotto_number not in lotto_numbers:
                lotto_numbers.append(lotto_number)
                break
    return lotto_numbers

def main():
    #추첨 회수를 입력받기
    num_of_lotto_draws = int(hw16_gui_input_code.gui_input("로또번호 6개르 몇 번 추출하시겠습니까?"))

    #num_of_lotto_draws개의 로또 번호 6개를 가진 리스트를 이차원 리스트를 받는다
    lotto_numbers = lotto_generator(num_of_lotto_draws)

    #num_of_lotto_draws만큼 추첨한 결과를 출력
    print("로또 번호 추첨 결과입니다:")
    for i in range(1, num_of_lotto_draws+1):
        print(f"{i}번째 추첨 번호: {lotto_numbers[i-1]}")

    #for문이 끝나고 프로그램을 종료한다
    print("\n프로그램이 종료되었습니다.")

if __name__ == "__main__":
    main()

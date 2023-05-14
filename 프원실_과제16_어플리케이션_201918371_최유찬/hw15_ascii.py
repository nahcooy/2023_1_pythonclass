import hw16_gui_input_code

def toggle_text(text: str):
    output_text = ""
    for c in text:
        if ord(c) >= 65 and ord(c) <= 90:
            output_text += chr(ord(c) + 32)
        elif ord(c) >= 97 and ord(c) <= 122:
            output_text += chr(ord(c) - 32)
        else:
            output_text += c
            #영어 알파벳이 아닌경우 예외처리

    print(output_text)

def caesar_encode(text: str, shift: int = 3):
    caesar_text = ""
    for c in text:
        if ord(c) >= 65 and ord(c) <= 90:
            shifted_c = ord(c) + shift
            if shifted_c > 90:
                shifted_c = shifted_c - 26
            caesar_text += chr(shifted_c)
        elif ord(c) >= 97 and ord(c) <= 122:
            shifted_c = ord(c) + shift
            if shifted_c > 122:
                shifted_c = shifted_c - 26
            caesar_text += chr(shifted_c)
        else:
            # 영어 알파벳이 아닌경우 예외처리
            caesar_text += c
    print(caesar_text)

def caesar_decode(caesar_text: str, shift: int = 3):
    decode_text = ""
    for c in caesar_text:
        if ord(c) >= 65 and ord(c) <= 90:
            shifted_c = ord(c) - shift
            if shifted_c < 65:
                shifted_c = shifted_c + 26
            decode_text += chr(shifted_c)
        elif ord(c) >= 97 and ord(c) <= 122:
            shifted_c = ord(c) - shift
            if shifted_c < 97:
                shifted_c = shifted_c + 26
            decode_text += chr(shifted_c)
        else:
            # 영어 알파벳이 아닌경우 예외처리
            decode_text += c
    print(decode_text)

def main():
    word = dict()
    word['ㄱㄴ'] = []  # 'ㄱㄴ' 키 추가
    filename = 'ㄱㄴ.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for w in line.split():
                word['ㄱㄴ'].append(w)
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("이용하고 싶은 기능의 번호를 입력하시오")
        print("1번: 문자열 대문자 소문자 변경")
        print("2번: 카이사르 암호")
        print("3번: 초성게임")
        print("1,2,3을 제외한 다른 문자를 입력하면 프로그램이 종료됩니다")


        n = hw16_gui_input_code.gui_input("이용하고 싶은 기능의 번호를 입력하시오\n1번: 문자열 대문자 소문자 변경\n2번: 카이사르 암호\n3번: 초성게임\n1,2,3을 제외한 다른 문자를 입력하면 프로그램이 종료됩니다")
        numlist = ['1', '2', '3']
        if n not in numlist:
            print("프로그램이 종료됩니다")
            break
        if n == '1':
            print("문자열 대문자 소문자 변경")
            text = hw16_gui_input_code.gui_input("문자열 대문자 소문자 변경\n영어 알파벳으로 구성된 문자열을 입력해주세요")
            toggle_text(text)
        if n == '2':
            print("카이사르 암호")
            checker = hw16_gui_input_code.gui_input("카이사르 암호\n암호문을 제작하려면 1, 암호문을 해독하려면 2를 입력해주세요\n1이나 2가 아닌 다른것이 입력되면 프로그램이 종료됩니다")
            if checker != '1' and checker != '2':
                print("프로그램이 종료됩니다")
                return
            if checker == '1':
                print("카이사르 암호 제작")
                text = hw16_gui_input_code.gui_input("카이사르 암호 제작\n암호문을 제작할 영어 알파벳으로 구성된 문자열을 입력해주세요")
                caesar_encode(text)
            if checker == '2':
                print("카이사르 암호 해독")
                text = hw16_gui_input_code.gui_input("카이사르 암호 해독\n암호문을 해독할 영어 알파벳으로 구성된 문자열을 입력해주세요")
                caesar_decode(text)

        if n == '3':
            print("초성게임을 시작합니다")
            for chosung in word:
                input_word = hw16_gui_input_code.gui_input(f"초성게임\n{chosung}을 초성으로 가진 단어를 입력해주세요")
                if input_word in word[chosung]:
                    print("맞았습니다")
                else:
                    print("틀렸습니다")
            print("초성게임을 종료합니다")
    return

if __name__=="__main__":
    main()
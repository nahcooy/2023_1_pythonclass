while True:
    try:
        n = int(input("정수를 입력해주세요 -> "))
        if n%2:
           print("입력하신 숫자는 홀수입니다")
        else:
            print("입력하신 숫자는 짝수입니다")
        break
    except:
        print("잘못된 입력입니다 다시 입력해주세요")
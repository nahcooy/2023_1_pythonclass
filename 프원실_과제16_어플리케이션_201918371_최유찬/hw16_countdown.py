import time
import winsound
import hw16_gui_input_code

def main():
    sec = int(hw16_gui_input_code.gui_input("초를 입력하세요: "))

    if sec <= 0:
        print("잘못된 숫자를 입력하였습니다, 0보다 큰 정수를 입력해주세요")
        exit(1)

    for remainsec in range(sec, 0, -1):
        print(remainsec)
        time.sleep(1)

    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

    print("\n프로그램이 종료됩니다")
    return

if __name__=="__main__":
    main()
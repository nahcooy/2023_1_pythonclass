import tkinter as tk

input_text = None  # 전역 변수로 선언

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
            # 영어 알파벳이 아닌 경우 예외 처리
            decode_text += c
    return decode_text

def decode_button_clicked():
    global input_text
    caesar_text = input_text.get("1.0", tk.END)
    decoded_text = caesar_decode(caesar_text)
    output_label.config(text=decoded_text)

def main():
    global input_text, output_label
    # GUI 윈도우 생성
    window = tk.Tk()
    window.title("Caesar Cipher Decoder")
    window.geometry("500x300")
    window.resizable(width=False, height=False)

    frm_entry = tk.Frame(master=window)
    frm_entry.grid(row=0, column=0, padx=10, pady=10)

    # "카이사르 암호: " 라벨
    caesar_label = tk.Label(master=frm_entry, text="카이사르 암호: ")
    caesar_label.grid(row=0, column=0, sticky="e")

    # 입력 텍스트 박스
    input_text = tk.Text(master=frm_entry, height=1, width=15)
    input_text.grid(row=0, column=1, padx=5)

    # 해독 버튼
    decode_button = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=decode_button_clicked)
    decode_button.grid(row=0, column=1, padx=10)

    # 출력 프레임
    output_frame = tk.Frame(master=window)
    output_frame.grid(row=0, column=2, padx=10)

    # 출력 라벨
    output_label = tk.Label(master=output_frame, text="")
    output_label.pack()

    # GUI 시작
    window.mainloop()

if __name__ == "__main__":
    main()

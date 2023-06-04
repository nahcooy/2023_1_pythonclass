import PySimpleGUI as sg

def caesar_encode(plain_text: str, shift: int = 3):
    encoded_text = ""
    for c in plain_text:
        if c.isalpha():
            if c.isupper():
                encoded_text += chr((ord(c) - 65 + shift) % 26 + 65)
            else:
                encoded_text += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            encoded_text += c
    return encoded_text

def caesar_decode(caesar_text: str, shift: int = 3):
    decoded_text = ""
    for c in caesar_text:
        if c.isalpha():
            if c.isupper():
                decoded_text += chr((ord(c) - 65 - shift) % 26 + 65)
            else:
                decoded_text += chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            decoded_text += c
    return decoded_text

sg.theme('DarkAmber')

layout = [
    [sg.Text('입력텍스트'), sg.InputText(key="-INPUTTEXT-")],
    [sg.Text('출력텍스트'), sg.InputText(key="-RESULT-")],
    [sg.Button('암호화'), sg.Button('복호화')]
]

window = sg.Window('Caesar Cipher', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "암호화":
        window['-RESULT-'].update(caesar_encode(values["-INPUTTEXT-"]))
    if event == "복호화":
        window['-RESULT-'].update(caesar_decode(values["-INPUTTEXT-"]))

window.close()

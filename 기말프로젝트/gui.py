import PySimpleGUI as sg
import 종목가져오기
import 주식가격예측
import 그래프그리기
import 주식정보
import 주식정보크롤링
import os
import threading

def show_stock_graph():
    if not os.path.exists('stock_codes.csv'):
        종목가져오기.stock_code_crawling()

    layout_graph = [
        [sg.Text('그래프로 보고싶은 주식 이름을 입력하세요:'), sg.InputText(key='stock_name'), sg.Button('→')],
        [sg.Canvas(key='graph_canvas')],
        [sg.Button('닫기')]
    ]

    window_graph = sg.Window('주식 그래프', layout_graph)

    while True:
        event, values = window_graph.read()

        if event == sg.WINDOW_CLOSED or event == '닫기':
            break

        if event == '→':
            stock_name = values['stock_name']
            if not stock_name:
                continue

            if 종목가져오기.stock_name_checker(stock_name):
                # 그래프 생성을 별도의 스레드로 실행
                graph_thread = threading.Thread(target=그래프그리기.graph, args=(stock_name,))
                graph_thread.start()
            else:
                sg.popup('존재하지 않는 주식입니다.')
                window_graph['stock_name'].update('')

    window_graph.close()

def stock_price_predicting():
    if not os.path.exists('stock_codes.csv'):
        종목가져오기.stock_code_crawling()

    layout_input = [
        [sg.Text('예측할 주식의 이름을 입력하세요:'), sg.InputText(key='predict_stock_name')],
        [sg.Text('예측에 고려한 기간을 선택하세요:'), sg.Combo(['1주일', '한달', '6개월', '1년'], key='predict_period'), sg.Button('→')],
    ]

    window_input = sg.Window('주식 그래프', layout_input)

    while True:
        event, values = window_input.read()

        if event == sg.WINDOW_CLOSED or event == '→':
            break

    window_input.close()

    predict_stock_name = values['predict_stock_name']
    predict_period = values['predict_period']

    if not 종목가져오기.stock_name_checker(predict_stock_name) :
        predict_stock_name = '랜덤'

    # 예측 주식 및 기간에 알맞은 그래프 출력
    df = 주식정보.save_graph_data_to_csv(predict_stock_name)

    # 그래프 그리기
    start_index, predict_period_day = 주식가격예측.plot_stock_graph(df, predict_period)

    # 새로운 창에서 예측 고점과 예측 저점 입력받기
    layout_expected = [
        [sg.Text('예상하는 고점을 입력하세요:'), sg.InputText(key='expected_high')],
        [sg.Text('예상하는 저점을 입력하세요:'), sg.InputText(key='expected_low')],
        [sg.Button('확인')]
    ]

    window_expected = sg.Window('예측 고점 및 저점', layout_expected)

    while True:
        event, values = window_expected.read()

        if event == sg.WINDOW_CLOSED or event == '확인':
            break

    window_expected.close()

    expected_high = values['expected_high']
    expected_low = values['expected_low']
    주식가격예측.plot_stock_graph_2(df, predict_period_day, start_index, expected_high, expected_low)

def show_stock_info():
    if not os.path.exists('stock_codes.csv'):
        종목가져오기.stock_code_crawling()

    layout_input = [[sg.Text('자세히 알고 싶은 주식의 이름을 입력하세요:'), sg.InputText(key='stock_name'), sg.Button('→')]]

    window_input = sg.Window('주식 정보', layout_input)

    while True:
        event, values = window_input.read()

        if event == sg.WINDOW_CLOSED or event == '→':
            break

    window_input.close()

    stock_name = values['stock_name']

    if not 종목가져오기.stock_name_checker(stock_name):
        sg.popup('존재하지 않는 주식입니다.')
        return

    code = 종목가져오기.find_stock_code(stock_name)
    stock_info = 주식정보크롤링.naver_finance_crawling(code)

    layout = [
        [sg.Text('주식 정보', font=('Helvetica', 20), justification='center')],
        [sg.Text(f'주식 이름: {stock_name}')],
        [sg.Text(f'현재가: {stock_info[0]}')],
        [sg.Text(f'시가: {stock_info[1]}')],
        [sg.Text(f'고가: {stock_info[2]}')],
        [sg.Text(f'저가: {stock_info[3]}')],
        [sg.Text(f'거래량: {stock_info[4]}')],
        [sg.Text(f'시가총액: {stock_info[5]}')],
        [sg.Text(f'시가총액순위: {stock_info[6]}')],
        [sg.Text(f'상장주식수: {stock_info[7]}')],
        [sg.Text(f'동일업종 등락률: {stock_info[8]}')],
        [sg.Button('닫기')]
    ]

    window = sg.Window('주식 정보', layout)

    while True:
        event, _ = window.read()

        if event == sg.WINDOW_CLOSED or event == '닫기':
            break

    window.close()




def main():
    layout = [
        [sg.Text('주식 Helper', font=('Helvetica', 20), justification='center')],
        [sg.Button('주식 그래프 보기', size=(30, 2))],
        [sg.Button('주식 가격 예측하기', size=(30, 2))],
        [sg.Button('주식 정보 보기', size=(30, 2))],
    ]

    window = sg.Window('주식 Helper', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == '주식 그래프 보기':
            show_stock_graph()
        elif event == '주식 가격 예측하기':
            stock_price_predicting()
        elif event == '주식 정보 보기':
            show_stock_info()

    window.close()

if __name__ == "__main__":
    main()

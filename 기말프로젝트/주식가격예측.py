import matplotlib.pyplot as plt
import random

def plot_stock_graph_2(df, period, start_index, expected_high=None, expected_low=None):
    end_index = start_index + period*2
    df_filtered = df[start_index:end_index]
    plt.plot(df_filtered['Date'], df_filtered['Close'], label='추가 그래프')

    if expected_high:
        expected_high = float(expected_high)
        plt.axhline(y=expected_high, color='r', linestyle='--', label='예상 고점')
    if expected_low:
        expected_low = float(expected_low)
        plt.axhline(y=expected_low, color='g', linestyle='--', label='예상 저점')

    # additional_point = end_index - period
    # plt.axvline(x=additional_point, color='b', linestyle='--', label='추가 지점')

    plt.xlabel('날짜')
    plt.ylabel('주가')
    plt.title('주식 그래프')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_stock_graph(df, period):
    # 데이터 필터링
    if period == '1주일':
        num_days = 7
    elif period == '한달':
        num_days = 30
    elif period == '6개월':
        num_days = 180
    elif period == '1년':
        num_days = 365
    else:
        print("유효하지 않은 기간입니다.")
        return None

    num_records = len(df)
    if num_records <= num_days:
        print("데이터가 충분하지 않습니다.")
        return None

    start_index = random.randint(0, num_records - num_days)
    end_index = start_index + num_days
    df_filtered = df[start_index:end_index]

    # 그래프 그리기
    plt.plot(df_filtered['Date'], df_filtered['Close'])

    plt.xlabel('날짜')
    plt.ylabel('주가')
    plt.title(f'{period} 주식 그래프')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return start_index, num_days

def main():
    pass

if __name__=="__main__":
    main()

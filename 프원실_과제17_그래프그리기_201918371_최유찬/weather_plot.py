import os
from typing import List
import requests
import matplotlib.pyplot as plt

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def download_weather(filename: str) -> None:
    """기상청에서 자료를 다운받아서 저장합니다."""
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19820101&endDt=20211231&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19810101&startYear=1981&endDay=20221231&endYear=2022&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", newline="") as f:
            f.write(res.text)

def str2float(text: str, default_value: float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        return default_value


def read_data(filename) -> (List[str], List[float], List[float]):
    """기상자료를 읽어서 날짜, 최저기온, 최고기온 리스트를 리턴합니다."""
    date_list = []
    tavg_list = []
    tmin_list = []
    tmax_list = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[8:]:
            line = line.strip()
            if line == "":
                continue
            tokens = line.split(",")
            date_list.append(tokens[0].split("-"))
            tavg_list.append(str2float(tokens[2], 999))
            tmin_list.append(str2float(tokens[3], 999))
            tmax_list.append(str2float(tokens[4], -999))

    return date_list, tavg_list, tmin_list, tmax_list


def get_month_days(month):
    # 1982년의 월별 일수를 반환합니다.
    for i in range(1, 12):
        month_days[i] += month_days[i-1]

    return month_days[month - 1]

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def find_index_of_date(month, date):
    date_index = list()

    primary_date_index = get_month_days(month) + date -1
    date_index.append(primary_date_index)

    for i in range(1983, 2022):
        if is_leap_year(i):
            primary_date_index += 366
            date_index.append(primary_date_index)
        else:
            primary_date_index += 365
            date_index.append(primary_date_index)
    return date_index

def main():
    # 1) 데이터 구해오기 (기상청)
    filename = "./history_jeonju.csv"
    download_weather(filename)

    # 2) 데이터 읽기 (주의: 빈 데이터 처리하기)
    dates, tavg, tmin, tmax = read_data(filename)

    # 3) 특정 날짜 입력받기
    print("특정날짜가 42년의 기간 중 몇 번째로 높은 기온인지를 출력하는 프로그램입니다")
    while True:
        print("특정날짜를 입력해주세요(ex: 2000-10-27) :", end=' ')
        year, month, date = map(int, input().split('-'))

        if 1982 <= year <= 2021 and 1 <= month <= 12 and 1 <= date <= month_days[month]:
            break
        else:
            print("올바른 연도, 월, 일을 다시 입력하세요.")

    # 4) 42년 간의 특정 날짜의 평균기온 데이터 가져오기
    date_index = find_index_of_date(month, date)

    year_index = year - 1982
    # 5) date_index에 해당하는 날짜의 평균기온 리스트로 만들기
    if tavg[year_index] == 999:
        print("해당 연도의 데이터를 찾을 수 없습니다.")
        return

    selected_tavg = []
    selected_years = []
    for i in date_index:
        if tavg[i] != 999:
            selected_tavg.append(tavg[i])
            selected_years.append(int(dates[i][0]))

    # 6) selected_tavg의 값들을 이용해서 선그래프 표현하기
    plt.rcParams["font.family"] = "Malgun Gothic"
    plt.rcParams["axes.unicode_minus"] = False

    # x축 눈금 레이블 설정
    plt.xticks(range(len(selected_tavg)), selected_years, rotation=75)

    plt.plot(selected_tavg, color="g", label="평균기온")
    plt.ylabel("기온(℃)")
    plt.legend()

    # 7) 특정 날짜의 평균기온 rank 표시 및 수평선 추가
    rank = sum(t > tavg[date_index[year_index]] for t in selected_tavg) + 1
    plt.axhline(tavg[date_index[year_index]], color="r", linestyle="-")  # 수평선 추가
    plt.text(date_index.index(date_index[year_index]) + 1, tavg[date_index[year_index]], f"{rank}번째", ha="left", va="center", color="b")

    # 특정 날짜의 점에 "o" 표시
    plt.plot(date_index.index(date_index[year_index]), tavg[date_index[year_index]], "bo")

    plt.show()

if __name__ == "__main__":
    main()

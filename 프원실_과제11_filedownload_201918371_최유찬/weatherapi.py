import requests
import os

def api2csv(URL):
    if os.path.exists("weather.csv"):
        pass
    else:
        with open("./weather.csv", "w", encoding="UTF-8-sig") as f:
            res = requests.get(URL)
            res.encoding = "UTF-8"
            f.write(res.text)
    return "weather.csv"

def csv2list(filename):
    with open(filename, 'r') as f:
        key = f.readline().strip().split(',')
        data = list()
        for line in f:
            data.append(list(map(float, line.strip().split(','))))
    return key, data


def raindata(data):
    return [float(value[9]) for value in data]


def count_rain_days(rainfall):  # 강수량이 0.1보다 클때만, 강우 일수에 포함한다
    raindays = 0
    for rain in rainfall:
        if rain > 0.1:
            raindays += 1
    return raindays


def sumifs(data):
    total_summer_rainfall = 0
    for value in data:
        if value[1] >= 6 and value[1] <= 8:
            total_summer_rainfall += value[9]
    return total_summer_rainfall


def longest_rain_days(rainfall):
    wettest_period = 0
    rain_days = 0

    for rain in rainfall:
        if rain > 0:
            rain_days += 1
            if rain_days > wettest_period:
                wettest_period = rain_days
        else:
            rain_days = 0

    return wettest_period


def maximum_rainfall_event(rainfall):
    maximum_rainfall = 0
    sum_of_rainfall = 0
    rain_days = 0

    for rain in rainfall:
        if rain > 0:
            rain_days += 1
            sum_of_rainfall += rain
            if rain_days > 2 and sum_of_rainfall >= maximum_rainfall:  # rain_days가 1보다 크면, 강우이벤트
                maximum_rainfall = sum_of_rainfall
        else:
            rain_days = 0
            sum_of_rainfall = 0

    return maximum_rainfall


def date_temp(data):
    dates = [[int(value[0]), int(value[1]), int(value[2])] for value in data]
    tmax = [float(value[3]) for value in data]
    tavg = [float(value[4]) for value in data]
    tmin = [float(value[5]) for value in data]
    return dates, tmax, tavg, tmin


def maximum_temp_gap(dates, tmax, tmin):
    max_temdif = 0
    max_temdif_date = None

    for i in range(len(dates)):
        if (tmax[i] - tmin[i]) > max_temdif:
            max_temdif = tmax[i] - tmin[i]
            max_temdif_date = dates[i]
    return max_temdif_date, max_temdif


def gdd(dates, tavg):
    integrated_temperature = 0
    for i in range(len(dates)):
        if dates[i][1] >= 5 and dates[i][1] <= 9 and tavg[i] > 5:
            integrated_temperature += tavg[i] - 5
    return integrated_temperature


def average(tavg):
    return sum(tavg) / len(tavg)


def topthree(tmax):
    cp_tmax = sorted(tmax, reverse=True)
    return cp_tmax[:3]


def main():
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    filename = api2csv(URL)
    key, data = csv2list(filename)
    rainfall = raindata(data)
    # print(key, data, rainfall, sep='\n') #list로 만든 데이터 확인

    with open("output.txt", 'w', encoding = "UTF-8-sig") as f:
        # 1
        f.write(f"총 강수량: {sum(rainfall):.1f}\n")
        # 2
        f.write("강우 일수: " + str(count_rain_days(rainfall)) + "\n")
        # 3
        f.write(f"여름철(6월-8월) 총 강수량: {sumifs(data):.1f}\n")
        # 4
        f.write("최장 연속 강우 일수: " + str(longest_rain_days(rainfall)) + "\n")
        # 5
        f.write(f"강우이벤트 중 최대 강수량: {maximum_rainfall_event(rainfall):.1f}\n")
        # 6
        dates, tmax, tavg, tmin = date_temp(data)
        max_temdif_date, max_temdif = maximum_temp_gap(dates, tmax, tmin)
        f.write(f"일교차가 가장 큰 날짜와 해당일자의 일교차: {max_temdif_date}, {max_temdif:.1f}\n")
        # 7
        f.write(f"5월부터 9월까지의 적산온도: {gdd(dates, tavg):.1f}\n")
        # 연평균 기온
        f.write(f"연평균 기온: {average(tavg):.1f}\n")
        # tmax 중 top3
        f.write(f"가장 높았던 최고기온 top3: {topthree(tmax)}입니다\n")
    print("output.txt에 정상적으로 저장되었습니다")
    # # 1
    # print(f"총 강수량: {sum(rainfall):.1f}")
    # # 2
    # print("강우 일수: ", count_rain_days(rainfall))
    # # 3
    # print(f"여름철(6월-8월) 총 강수량: {sumifs(data):.1f}")
    # # 4
    # print("최장 연속 강우 일수: ", longest_rain_days(rainfall))
    # # 5
    # print(f"강우이벤트 중 최대 강수량: {maximum_rainfall_event(rainfall):.1f}")
    # # 6
    # dates, tmax, tavg, tmin = date_temp(data)
    # max_temdif_date, max_temdif = maximum_temp_gap(dates, tmax, tmin)
    # print(f"일교차가 가장 큰 날짜와 해당일자의 일교차: {max_temdif_date}, {max_temdif:.1f}")
    # # 7
    # print(f"5월부터 9월까지의 적산온도: {gdd(dates, tavg):.1f}")
    # # 연평균 기온
    # print(f"연평균 기온: {average(tavg):.1f}")
    # # tmax 중 top3
    # print(f"가장 높았던 최고기온 top3: {topthree(tmax)}입니다")

if __name__ == "__main__":
    main()

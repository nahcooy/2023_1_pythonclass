def csv2list(filename):
    with open(filename, 'r') as f:
        key = f.readline().strip().split(',')
        data = list()
        for line in f:
            data.append(list(map(float, line.strip().split(','))))

    return key, data

def raindata(data):
    return [float(value[9]) for value in data]

def count_rain_days(rainfall): #강수량이 0.1보다 클때만, 강우 일수에 포함한다
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
            if rain_days > 2 and sum_of_rainfall >= maximum_rainfall: #rain_days가 1보다 크면, 강우이벤트
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

def maximum_temp_gap(dates, tmax , tmin):
    max_temdif = 0
    max_temdif_date = None

    for i in range(len(dates)):
        if (tmax[i]-tmin[i]) > max_temdif:
            max_temdif = tmax[i]-tmin[i]
            max_temdif_date = dates[i]
    return max_temdif_date, max_temdif
def gdd(dates, tavg):
    integrated_temperature = 0
    for i in range(len(dates)):
        if dates[i][1] >= 5 and dates[i][1] <= 9 and tavg[i]>=15:
            integrated_temperature += tavg[i] - 15
    return integrated_temperature

def main():
    filename = "weather.csv"
    key, data = csv2list(filename)
    rainfall = raindata(data)
    #print(key, data, rainfall, sep='\n') #list로 만든 데이터 확인
    # 1
    print(f"총 강수량: {sum(rainfall):.1f}")
    # 2
    print("강우 일수: ", count_rain_days(rainfall))
    # 3
    print(f"여름철(6월-8월) 총 강수량: {sumifs(data):.1f}")
    # 4
    print("최장 연속 강우 일수: ", longest_rain_days(rainfall))
    #5
    print(f"강우이벤트 중 최대 강수량: {maximum_rainfall_event(rainfall):.1f}")
    # 6
    dates, tmax, tavg, tmin = date_temp(data)
    max_temdif_date,  max_temdif = maximum_temp_gap(dates, tmax, tmin)
    print(f"일교차가 가장 큰 날짜와 해당일자의 일교차: {max_temdif_date}, {max_temdif:.1f}")
    #7
    print(f"5월부터 9월까지의 적산온도: {gdd(dates, tavg):.1f}")

if __name__=="__main__":
    main()
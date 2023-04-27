import hw12_submission

def csv2list(filename):
    with open(filename, 'r') as f:
        key = f.readline().strip().split(',')
        data = list()
        for line in f:
            data.append(list(map(float, line.strip().split(','))))

    return key, data

def date(data):
    rain_fall = list()
    tmm = list()
    for x in data:
        year = str(int(x[0]))
        month = str(int(x[1]))
        if len(month) == 1:
            month = '0' + month
        day = str(int(x[2]))
        if len(day) == 1:
            day = '0' + day
        ymd = year + '-' + month + '-' + day
        rain_fall.append([ymd, x[9]])
        tmm.append([ymd, x[3], x[5]])

    return rain_fall, tmm

def maxrainfall(rain_fall):
    mrd, mr = rain_fall[0][0], rain_fall[0][1]
    for i in range(1, len(rain_fall)):
        if rain_fall[i][1] > mr:
            mrd, mr = rain_fall[i][0], rain_fall[i][1]
    return mrd, mr

def maxtemp(tmm):
    tmaxd, tmax = tmm[0][0], (tmm[0][1]-tmm[0][2])
    for i in range(1, len(tmm)):
        if (tmm[i][1] - tmm[i][2]) > tmax:
            tmaxd, tmax = tmm[i][0], (tmm[i][1]-tmm[i][2])
    return tmaxd, tmax

def main():
    myname = "최유찬"
    filename = "weather146.csv"
    key, data = csv2list(filename)
    rain_fall, tmm = date(data)
    max_rainfall_date, max_rainfall = maxrainfall(rain_fall)
    temp_max_date, temp_max = maxtemp(tmm)
    print(myname, max_rainfall, max_rainfall_date, temp_max, temp_max_date, " 가 과제에 제출되었습니다")
    hw12_submission.submit(myname, max_rainfall, max_rainfall_date, temp_max, temp_max_date)

if __name__ == "__main__":
    main()

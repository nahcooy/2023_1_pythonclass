import hw13_submission

def csv2list(filename):
    with open(filename, 'r') as f:
        key = f.readline().strip().split(',')
        data = list()
        for line in f:
            data.append(list(map(float, line.strip().split(','))))

    return key, data

def date(data):
    tmm = list()
    for x in data:
        ymd = f"{int(x[0]):02d}-{int(x[1]):02d}-{int(x[2]):02d}"
        tmm.append([ymd, x[3], x[5]])

    return tmm

def maxtemp(tmm):
    tgmaxd, tgmax = tmm[0][0], (tmm[0][1]-tmm[0][2])
    tmaxd, tmax = tmm[0][0], tmm[0][1]
    for i in range(1, len(tmm)):
        if (tmm[i][1] - tmm[i][2]) > tgmax:
            tgmaxd, tgmax = tmm[i][0], (tmm[i][1]-tmm[i][2])
        if tmm[i][1] > tmax:
            tmaxd, tmax = tmm[i][0], tmm[i][1]
    return tmaxd, tmax, tgmaxd, tgmax

def main():
    myname = "최유찬"
    filename = "weather140.csv"
    key, data = csv2list(filename)
    tmm = date(data)
    max_temp_date, max_temp, tempgap_max_date, tempgap_max = maxtemp(tmm)
    print(myname, max_temp, max_temp_date, tempgap_max, tempgap_max_date, "가 과제에 제출되었습니다")
    hw13_submission.submit(myname, max_temp, max_temp_date, tempgap_max, tempgap_max_date)

if __name__ == "__main__":
    main()

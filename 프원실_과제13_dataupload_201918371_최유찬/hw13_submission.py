import requests

def submit(name: str, rain_max: float, rain_max_date: str, gap_max: float, gap_max_date: str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbyNex1PwGoPeR9Be--QlYrD90C8CR6FU_CC82K2EaGrc2-uVHtbHOw7ZwjfNTESHA5Eiw/exec"
    PARAMS = {
        '제출자': name,
        '최고기온': rain_max,
        '최고기온날짜': rain_max_date,
        '최대일교차': gap_max,
        '최대일교차날짜': gap_max_date,
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")

if __name__ == "__main__":
    submit("홍길동", 340.1, "2011-08-04", 25.2, "1978-01-04")

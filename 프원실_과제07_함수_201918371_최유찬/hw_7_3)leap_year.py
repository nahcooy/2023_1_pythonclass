#과제 #07 - 3) 연도(y)를 주면, 윤년인지(True) 아닌지를(False) 알려주는 is_leap_year(y) 함수를 만드시오.
import calendar

def is_leap_year1(y): #if문을 2번 이용하여 윤년인지 아닌지 판단
    if y % 4 == 0:
        if y % 100 == 0:
            return False
        else:
            return True
    else:
        return False

def is_leap_year2(y): #if문에 and를 이용하여 if문을 한번만 사용하여 윤년인지 아닌지 판단
    if y % 4 == 0 and y % 100 != 0:
        return True

    else:
        return False


def is_leap_year3(y):  #calendar 라이브러리를 이용한 윤년 판단
    return calendar.isleap(y)

def main():
    year = int(input("윤년인지 아닌지를 판단할 연도를 입력해주세요\n"))
    print("{}는 윤년이 {}입니다".format(year, is_leap_year1(year)))

if __name__ == "__main__":
	main()
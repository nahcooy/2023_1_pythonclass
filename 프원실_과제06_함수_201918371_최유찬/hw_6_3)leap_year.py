#과제 #06 - 3) 연도(y)를 주면, 윤년인지(True) 아닌지를(False) 알려주는 is_leap_year(y) 함수를 만드시오.

def is_leap_year(y):
    if y%4 ==0:
        if y%100==0:
            return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("윤년인지 아닌지를 판단할 연도를 입력해주세요\n"))
    print("{}는 윤년이 {}입니다".format(year, is_leap_year(year)))

if __name__ == "__main__":
	main()
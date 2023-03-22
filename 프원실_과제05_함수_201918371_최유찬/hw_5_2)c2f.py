#과제 #05 - 2)섭씨를 화씨로 바꾸는 함수 c2f(t_c) 함수를 만드시오.

def c2f(t_c):
    t_f = (t_c * 1.8) + 32
    print("{:.1f} degrees Celsius is {:.1f} Fahrenheit".format(t_c, t_f))

def main():
    t_c = int(input("Please enter the Celsius temperature -> "))
    c2f(t_c)

if __name__ == "__main__":
	main()
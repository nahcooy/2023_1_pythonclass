#과제 #03 - 1)실습01 완성하기 - 섭씨를 화씨로 변환하는 프로그램 (input 이용)

temp_c = input("Celsius to Fahrenheit\nEnter a temperature in Celsius ")
temp_c = int(temp_c)

temp_f = (temp_c*1.8)+32

print("{:.1f} degrees Celsius is {:.1f} Fahrenheit".format(temp_c, temp_f))
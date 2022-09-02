# mins = 59
# hour = 60
# x = mins/hour
# print(round(x,2))
# y = mins//hour
# print(y)

# # + cộng - plus
# # - trừ - minus
# # * nhân - time, mutiply/mutiplied
# # / chia - division/ divided
# # // - chia làm tròn
# # ** - mũ
# # % là chia lấy số dư

# x = 5
# a = x + 5
# print(a)

# print("------------------------")

# x = 10
# y = 9
# a = x % y
# print(a)

# print("------------------------")

# a = "Nguyen "
# b = "Duy"
# c = a + b
# print(c)

# print("------------------------")
# # Ex 1
# name = input("Enter Your Name: ")
# print("Your name is",name)

# print("------------------------")
# # Ex 2
# hours = int(input("Enter Hours: "))
# rate = int(input("Enter Rate: "))
# result = hours*rate
# print("Pay: " + str(result))

# print("---------------------")
# # Ex 3
# width = float(input("Enter the Width: "))
# height = float(input("Enter the Height: "))

# print("Value is : ", width // 2 ,"and type is: " ,type(width // 2))
# print("Value is : ", width / 2.0 ,"and type is: " , type(width / 2.0))
# print("Value is : ", round(width / 3,2) ,"and type is: " , type(width / 3))
# print("Value is :" , 1 + 2 * 5,"and type is: " , type(1 + 2 * 5))
# #type(phep tinh) để biết dạng số của kết quả phép tính : float,int,...

# print("--------------")
# # USD convert to K VND
# USD = input("Nhap so USD: ")

# VND = int(USD) * 23 


# print("---")
# print(str(USD),"=",str(VND),"K VND")

# print("----------------")
# # Ex 4
# # oC --> oF
# celsius = float(input("Enter the degrees outside ( C degrees ): "))
# fahrenheit = (celsius*1.8)+32
# #dùng công thức 
# print("The",celsius,"C degrees equal",":",fahrenheit,"F degrees")

# print("---------------")
# # Ex 5:
# # Rewrite your pay computation to give the employee 1.5
# # times the hourly rate for hours worked above 40 hours.


# hours = float(input("Hours works: "))
# rate = float(input("Rate work: "))
# overtime_work = hours - 40
# pay_enough_hours = 40 * rate
# rate_per_hours = 1.5 * rate

# if hours <= 40:
#     pay = (hours*rate)
# elif hours > 40:
#     pay = (overtime_work * rate_per_hours + pay_enough_hours)

# print("Pay: ",pay)

# print("----")
# # Ex 6:
# # Rewrite your pay computation to give the employee 1.5
# # times the hourly rate for hours worked above 40 hours.
# # if hours and rates are str. Output will be (Please Enter numberic answer)

# try:
#     hours = input("Hours works: ")
#     int(hours)
#     rates = input("Rate work: ")
#     int(rates)
#     print("Pay: ",(hours - 40,1) * (1.5*rates) + (40*rates))
# except:
#     print('Enter numberic input')

# # Sử dụng Try và Except
# # Trong Try check nếu hours là int thì tiếp tục check rate là int 
# # except: nếu hours và rate ko phải là float hay int thì print("Please...")

# print("---")

# # Exercise 7: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is
# # between 0.0 and 1.0, print a grade using the following table:
# # >= 0.9 A
# # >= 0.8 B
# # >= 0.7 C
# # >= 0.6 D
# # < 0.6 F
# # Enter score: 0.95
# # A
# # Enter score: perfect
# # Bad score
# # Enter score: 10.0
# # Bad score
# # Enter score: 0.75
# # C
# # Enter score: 0.5
# # F

# score = float(input("Score: "))

# try:
#     float(score)
#     if score >= 0.9 and score <= 1.0:
#         print("Grade A")
#     elif score >= 0.8 and score <= 0.9:
#         print("Grade B")
#     elif score >= 0.7 and score <= 0.8:
#         print("Grade C")
#     elif score >= 0.6 and score <= 0.7:
#         print("Grade D")
#     elif score < 0.6 and score > 0.0:
#         print("Grade F")
#     else:
#         print("Out of range!!!")
    
# except:
#     print("Error")
    
# print("---")
# Exercise 8:
# re-write Ex 6 use Function

# import datetime

# def ask_employee_info(name,numbers_of_employee):
#     today = datetime.datetime.now()
#     print("---------------------")
#     print(today)
#     print("Your name is: ",name)
#     print("Indentification numbers: ",numbers_of_employee)

# def compute_pay(hours,rates):
#     overtime_work = hours - 40
#     rate_per_hours = 1.5 * rates
#     pay_employee = 40 * rates
#     if hours == 40:
#         pay = pay_employee
#     elif hours > 40:
#         pay = (overtime_work * rate_per_hours + pay_employee)
#     else:
#         print("Not enought hours work this month")
    
#     print("Pay: ",pay,"$")

# def main():
#     name = input("Enter the employee name: ")
#     employee_numbers = input("Type your identification number: ")
#     hours = float(input("Hours work: "))
#     rates = float(input("Rates: "))

#     ask_employee_info(name,employee_numbers)
#     compute_pay(hours,rates)

# main()

# print("-------")
# Exercise 9:
# re-write Ex 7 use function

# score = float(input("Score: "))
# try:
#     score = float(score)
#     def computegrade():
#         if score >= 0.9 and score <= 1.0:
#             print("Grade A") 
#         elif score >= 0.8 and score <= 0.9:
#             print("Grade B") 
#         elif score >= 0.7 and score <= 0.8:
#             print("Grade C") 
#         elif score >= 0.6 and score <= 0.7:
#             print("Grade D") 
#         elif score < 0.6 and score > 0.0:
#             print("Grade F") 
#         else:
#             print("Out of range!!!") 
#     computegrade()

# except:
#     print("Error")

from operator import length_hint


print("---")
# Exercise 10:
# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')
# The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.

# Write a function that draws a similar grid with four rows and four column

# def func_1():
#     print("+", 4*'-', '+', 4*'-', '+', 4*'-', '+')


# def func_2():
#     for x in range(4):
#         print('|', 4*' ', '|', 4*' ', '|', 4*' ', '|')


# def draw():
#     func_1()
#     func_2()
#     func_1()
#     func_2()
#     func_1()
#     func_2()
#     func_1()


# draw()

# print("---")

# # Exercise 10
# total = 0
# count = 0
# numbers = 0
# while True:
#     try:
#         number_x = input("Enter a number: ")
#         if number_x == "done":
#             break
#         number = float(number_x)
#         total = total + number
#         count = count + 1
#         average = total/count
#     except:
#         print("Error, Try again")
# print("total: ",total,",","count: ",count,",","average: ",",",average)

# print("---")
# # Exercise 11: Write another program that prompts for a list of numbers
# # as above and at the end prints out both the maximum and minimum of
# # the numbers instead of the average

# largest = None
# smallest = None
# total = 0
# count = 0
# average = 0
# while True:
#     try:
#         numbers = input("Enter numbers: ")
#         if numbers == "done":
#             break
#         numbers = float(numbers)
#         total =+ numbers
#         count = count + 1
#         average = total/count
#         if largest == None and smallest == None:
#             largest = numbers
#             smallest = numbers
#         if largest == None or numbers > largest:
#             largest = numbers
#         if smallest == None or numbers < smallest:
#             smallest = numbers
#     except:
#         print("Error,please enter numberic input")
# print("total: ",total,"count: ",count,"average: ", round(average,1))
# print("Largest number: ", largest,",","Smallest number: ", smallest)

# # print apple
# fruit = 'apple'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     ndex = index + 1

# # print apple --> elppa
# fruit = "apple"
# index = 0
# try:
#     while index < len(fruit): # khi 0 < độ dài của fruit = 5
#         index = index -1 # nếu mà + 1 = apple thì => -1 là ngược lại
#         print_screen = fruit[index]
#         print(print_screen)
# except:
#     while True:
#         break

# print apple 2
# fruit = "apple"
# for i in range(0, len(fruit)): # 0,1,2,3,4
#     print(fruit[i], end="") 

# print apple - elppa 2
#fruit = "apple"
#for i in fruit[::-1]:
#    print(fruit[i])

# Exercise 12: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
# Another way to write a traversal is with a for loop:

# fruit = "apple"
# index = 0
# try:
#     while index < len(fruit):
#         index = index -1
#         print_screen = fruit[index]
#         print(print_screen)
# except:
#     while True:
#         break

# a = "FishEatBurger"
# # a[start:stop:step]
# print(a[::-1])
# print(a[4:])
# print(a[:4])
# print(a[::])

# word = "peanuts"
# if word < 'banana':
#     print('Your word,' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word,' + word + ', comes after banana.')
# else:
#     print('All right, bananas.')

a = input()
print(len(a))

b = a.strip()

print(len(a))

print("---")

txt = "herewego"

x = txt.lstrip("here")
a = txt.rstrip("go")

print(x)
print(a)

print("---")
a = "Hello aldald"
x = a.find("o")
print(x)




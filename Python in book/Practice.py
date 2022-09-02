#-------------------------------
# Part 1: Conditional execution
#-------------------------------
# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
money_pay = 40 * rate
overtime_work = hours - 40
rate_per_hours = 1.5 * rate

if hours == 40:
    pay = money_pay
elif hours > 40:
    pay = (overtime_work * rate_per_hours + money_pay)
else:
    print("Not enough work time!!!")

print("Pay: ",pay)

# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    hours = input("Enter hours: ")
    int(hours)
    rate = input("Enter rate: ")
    int(rate)
    print("hours: ",hours)
    print("rate: ",rate)
except:
    print("Error, please enter numeric input")

# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# 3.11. EXERCISES 41
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input

score = input("Enter score: ")

try:
    score = float(score)
    if score >= 0.9 and score <= 1.0:
        print("Grade A")
    elif score >= 0.8 and score < 0.9:
        print("Grade B")
    elif score >=0.7 and score < 0.8:
        print("Grade C")
    elif score >= 0.6 and score < 0.7:
        print("Grade D")
    elif score < 0.6 :
        print("Grade F")
    else:
        print("Out of range!")

except:
    print("Error,try again")

# ----------------
# Part 2: Function
# ----------------
# Exercise 4: Rewrite your pay computation with time-and-a-half for over_time and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

import datetime

def print_employee_info(name,number_of_employee):
    today = datetime.datetime.now()
    today_2 = today.now()
    print("\n")
    print(today_2)
    print("-----------------------")
    print("Employee's name is :",name)
    print("Employee's number is: ",number_of_employee)

def compute_pay(hours,rate):
    money_pay = 40 * rate
    overtime_work = hours - 40
    rate_per_hours = 1.5 * rate

    if hours == 40:
        pay = money_pay
    elif hours > 40:
        pay = (overtime_work * rate_per_hours + money_pay)
    else:
        print("Not enough work time!!!")

    print("Pay: ",pay,"$")

def main():
    ask_name = input("What is a employee's name: ")
    number_of_employee = input("His/her number is: ")
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))

    compute_pay(hours,rate)
    print_employee_info(ask_name,number_of_employee)

main()

# Exercise 5: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# 4.14. EXERCISES 55
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly to test the various different values for input.


import numbers


def computegrade(score):
    try:
        score = float(score)
        if score >= 0.9 and score <= 1.0:
            print("Grade A")
        elif score >= 0.8 and score < 0.9:
            print("Grade B")
        elif score >=0.7 and score < 0.8:
            print("Grade C")
        elif score >= 0.6 and score < 0.7:
            print("Grade D")
        elif score < 0.6 :
            print("Grade F")
        else:
            print("Out of range!")

    except:
        print("Error,try again")

def main():
    score = input("Enter score: ")
    computegrade(score)

main()

# ----------------
#Part 3: Interation
# ----------------
# Exercise 6: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

total = 0
count = 0
average = 0

while True:
    try:
        number_input = input("Enter the number: ")
        if number_input == "done":
            break
        number_input = float(number_input)
        total = total + number_input
        count = count + 1
        average = total/count
    except:
        print("bad data")

print("Total: ",total)
print("Count: ",count)
print("Average: ",average)

# Exercise 7: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average

maximum_number = None
minxinmum_number = None
total = 0
count = 0
average = 0

while True:
    try:
        number_input = input("Enter the number: ")
        if number_input == "done":
            break
        number_input = float(number_input)
        total = total + number_input
        count = count + 1
        average = total/count
        if maximum_number is None or number_input > maximum_number:
            maximum_number = number_input
        if minxinmum_number is None or number_input < minxinmum_number:
            minxinmum_number = number_input
    except:
        print("bad data")

print("Total: ",total)
print("Count: ",count)
print("Average: ",average)
print("Largest number: ",maximum_number)
print("Smallest number: ",minxinmum_number)

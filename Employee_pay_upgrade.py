import datetime

def write_info_to_text(computepay,name,number_of_employee,hours,rate):
    f_name = input("Enter the file name to create: ")
    with open(f_name,"w") as file:
        file.write("Employee name is: " + name + "\n")
        file.write("Employee number if: " + number_of_employee + "\n")
        file.write("Hours work: " + str(hours) + "\n")
        file.write("Rate work: " + str(rate) + "\n")
        file.write("Pay: " + str(computepay) + "\n")

def print_info_employee(name,number_of_employee):
    today = datetime.datetime.now()
    print("--------------------")
    print(today)
    print("Employee name is: ",name)
    print("Employee number is: ",number_of_employee)


def compute_pay(hours,rate):
    overtime_work = hours - 40
    rate_per_hours = 1.5 * rate
    pay_for_employee = 40 * rate
    try:
        hours = float(hours)
        rate = float(rate)
        if hours == 40:
            pay = pay_for_employee
        elif hours > 40:
            pay = (overtime_work * rate_per_hours + pay_for_employee)

        print("Pay: ",pay)
        return pay
    except:
        print("You must enter numberic input")

def main():
    name = input("Enter employee name: ")
    number_of_employee = input("Enter number of employee: ")
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))

    print_info_employee(name,number_of_employee)
    computepay = compute_pay(hours,rate)
    write_info_to_text(computepay,name,number_of_employee,hours,rate)

main()
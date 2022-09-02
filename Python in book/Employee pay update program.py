import datetime

def write_info_to_text(pay,hours,rates,name,numbers_of_employee):
    print("-------")
    f_name = input("Enter the file name: ")
    with open(f_name, "w") as file:
        file.write("Employee name is: " + name +"\n")
        file.write("Employee number: " + numbers_of_employee + "\n")
        file.write("Hours work: "+ str(hours) +"\n")
        file.write("Rate: " + str(rates) + "\n")
        file.write("Pay: " + str(pay) + "\n")        

def ask_employee_info(name,numbers_of_employee):
    today = datetime.datetime.now()
    print("---------------------")
    print(today)
    print("Your name is: ",name)
    print("Indentification numbers: ",numbers_of_employee)
    return name,numbers_of_employee

def compute_pay(hours,rates):
    overtime_work = hours - 40
    rate_per_hours = 1.5 * rates
    pay_employee = 40 * rates
    if hours == 40:
        pay = pay_employee
    elif hours > 40:
        pay = (overtime_work * rate_per_hours + pay_employee)
    else:
        print("Not enought hours work this month")
    
    print("Pay:",pay)
    return pay

def main():
    name = input("Enter the employee name: ")
    employee_numbers = input("Type your identification number: ")
    hours = float(input("Hours work: "))
    rates = float(input("Rates: "))

    ask_employee_info(name,employee_numbers)
    pay = compute_pay(hours,rates)
    write_info_to_text(pay,hours,rates,name,employee_numbers)

main()
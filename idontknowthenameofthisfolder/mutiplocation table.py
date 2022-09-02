while True:
    try:
        print("---------------------------")
        print("Enter 'Quit' to exit program")
        number = input("Enter number: ")
        if number == "Quit":
            break
        number = int(number)
        for i in range(1,11):
            result = number * i
            print("--------------------")
            print(number,"x",i,"=",result)
    except:
        print("Please enter numberic input")
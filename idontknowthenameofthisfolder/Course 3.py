### LESSON 3: NESTED LOOP

rows = int(input("How many rows: "))
column = int(input("How many columns: "))
symbol = input("Enter the symbol you want: ")

for i in range(rows):
    for j in range(column):
        print(symbol , end=" ")
    print()                     #vì có 2 for loop nên print(symbol) cho j còn print()cho i
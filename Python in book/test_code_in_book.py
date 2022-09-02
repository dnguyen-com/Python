# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# print("---")

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# print("---")

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')

# print("---")

# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
# print('Count: ', count)

# print("---")
# largest = None
# print('Before:', largest)
# for i in [3, 41, 12, 9, 74, 15]:
#     if largest is None or i > largest :
#         largest = i
#     print('Loop:', i, largest)
# print('Largest:', largest)

# b = [20, 10, 5]
# # b có 3 phần tử 20,10,5
# total = 0 # tổng lúc đầu = 0
# for a in b: # a sẽ chạy lần lượt (20,10,5)
#     total = total + a
    # 0   =   0   + 20
    # Update--> 20 = 20 + 10
    # Update--> 30 = 30 + 5
    # End vì đã chạy hết 3 phần tử trong b
# print(total)

# c = list(range(1,5))
# print(c)
# # đổi qua dạng list

# total2 = 0
# for i in range(1,5):
#     total2 =+ i
# print(total2)

# total3 = 0
# for i in range(1,8):
#     if i % 3 == 0:
#         total3 += i
# print(total3)

sum = 0
count = 0
average = 0

while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"): 
     break
    value = float(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input.")
print (sum, count, average)
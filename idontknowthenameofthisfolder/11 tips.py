# 1/ Interate with enumerate() instead of range(len())

data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)

data = [1, 2, -3, -4]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)

print("----")
# 2/ Use list comprehensions instead of for raw loops

squares = []
for i in range(10):
    squares.append(i*i)

print(squares)

squares = [i*i for i in range(10)]
print(squares)

print("----")
# 3/ Sort complex interables with sorted()

data = [3, 5, 1, 10, 9]
sorted_data = sorted(data, reverse=True) # reverse=True for descending biggest to smallest

print(sorted_data)

data = [{"name": "Max", "age": 6},
        {"name": "Max", "age": 20},
        {"name": "Max", "age": 9}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

print("----")
# 4/ Stores unique values with Sets()

data = [1,2,3,4,5,5,5,5,5]
data_2 = set(data)
print(data_2)

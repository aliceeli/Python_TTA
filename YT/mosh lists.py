names = ["John", "Bob", "Sarah", "Alice", "Mosh"]
names[0] = "Jon"
print(names[:])

numbers = [3, 7, 9, 4, 1]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

for row in matrix:
    for item in row:
        print(item)
print()

numbers = [5, 3, 7, 4, 9]
numbers2 = numbers.copy()
numbers.append(13)
numbers.insert(0, 10)
numbers.remove(7)
#numbers.clear()
numbers.pop()
print(numbers.index(3))
print(numbers)
print(50 in numbers)
print(4 in numbers)
numbers.append(4)
print(numbers.count(4))
numbers.sort()
numbers.reverse()
print(numbers2)
print(numbers)

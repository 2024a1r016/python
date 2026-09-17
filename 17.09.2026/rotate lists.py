#wap a program to rotate a list one position to the right.
n = int(input("Enter total numbers: "))

numbers = []

for i in range(n):
    m = int(input("Enter number: "))
    numbers.append(m)

last = numbers[-1]

for i in range(n - 1, 0, -1):
    numbers[i] = numbers[i - 1]

numbers[0] = last

print("List after right rotation:", numbers)
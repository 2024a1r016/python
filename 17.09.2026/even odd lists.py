#wap to input numbers in a list and create two seperate lists for even and odd numbers.
n = int(input("Enter total numbers: "))

numbers = []
even = []
odd = []

for i in range(n):
    m = int(input("Enter number: "))
    numbers.append(m)

for m in numbers:
    if m % 2 == 0:
        even.append(m)
    else:
        odd.append(m)

print("Even numbers:", even)
print("Odd numbers:", odd)
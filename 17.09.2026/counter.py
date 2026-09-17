#wap to count how many times a particular item appears in a list
n = int(input("Enter total numbers: "))

numbers = []

for i in range(n):
    m = int(input("Enter number: "))
    numbers.append(m)

item = int(input("Enter item to count: "))

count = numbers.count(item)

print("The item appears", count, "times.")
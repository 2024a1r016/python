#wap to input a list of numbers and create a new list containing only unique elements.
n=int(input("Enter elements: "))
numbers=[]
unique=[]

for i in range(n):
    m=int(input("Enter elements: "))
    numbers.append(m)

for m in numbers:
    if m not in unique:
        unique.append(m)

print("Unique Elements: ",unique)
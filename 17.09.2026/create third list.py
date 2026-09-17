#wap to input two lists and create a third list containing common elements.
n1 = int(input("Enter total elements in first list: "))

list1 = []

for i in range(n1):
    m = int(input("Enter number: "))
    list1.append(m)

n2 = int(input("Enter total elements in second list: "))

list2 = []

for i in range(n2):
    m = int(input("Enter number: "))
    list2.append(m)

common = []

for m in list1:
    if m in list2:
        common.append(m)

print("First list:", list1)
print("Second list:", list2)
print("Common elements:", common)
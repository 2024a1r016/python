#wap to check whether a given value is present in a tuple. If present, display its position.
t = (10, 20, 30, 40, 50)
n = int(input("Enter value to search: "))
if n in t:
    print("Value is present")
    print("Position:", t.index(n))
else:
    print("Value is not present")
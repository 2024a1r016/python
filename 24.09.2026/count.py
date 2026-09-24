#wap to store repeated values in a tuple and count how many times a given value appears.
t = (10, 20, 10, 30, 20, 10, 40, 10)
print("Tuple:", t)
n = int(input("Enter value to count: "))
count = t.count(n)
print(n, "appears", count, "times")
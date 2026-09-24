#wap to show that tuple values cannot be changes directly. Convert tuple into list, update it, and convert it back into tuple.
t = (10, 20, 30, 40)
print("Original tuple:", t)
l = list(t)
l[1] = 25
t = tuple(l)
print("Updated tuple:", t)
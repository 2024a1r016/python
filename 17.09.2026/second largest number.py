#wap to input numbers in a list and find the second largest number
n=int(input("Enter total numbers to input: "))
numbers=[]

for i in range(n):
  m=int(input("Enter number: "))
  numbers.append(m)

numbers.sort()

print("Second Largest Number: ",numbers[-2])

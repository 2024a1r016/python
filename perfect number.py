#wap to check whether a number is perfect number. A number is perfect if the sum of its proper divisors is equal to the number itself

num = int(input("Enter a number: "))
divisor_sum = 0
for i in range(1,num):
    if num % 1==0:
        divisor_sum+=i
if divisor_sum==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is NOT a perfect number")
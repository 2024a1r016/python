#wap to input a number and check whether it is prime or not.A number is prime if it has no divisor other than 1 itself
num=int(input(" "))
is_prime=True
if(num<=1):
 is_prime=False
else:
 for i in range(2,num):
  if num%i==0:
   is_prime=False
  break
if is_prime:
 print("Prime")
else:
 print("Not prime")
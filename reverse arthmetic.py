#wap to input a number and reverse it using arthmetic operations only

a = int(input("Enter first number: "))
rev = 0
while a>0:
    digit = a%10
    rev = rev * 10 + digit

    a = a//10
print("Reverse: ",rev)
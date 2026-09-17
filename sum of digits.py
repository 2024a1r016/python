#wap to print number to repeatedly calculate the sum of digits of a number until the result becomes a single digit.
#Example: 9875 -> 9 + 8 + 7 + 5 = 29 -> 2 + 9 = 11 -> 1 + 1 = 2
no = int(input("Enter the number: "))

while no >= 10:
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    no = sum

print("Single digit result:", no)
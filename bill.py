"""WAP to calculate the final bill amount after applying a discount.The program should take the total bill amount as input from the user and apply the discount according to the following rules.After calculating the discount,the program should display the discount amount and the final bill amount payable by te customer
above 5000-20 % discount, 3000-5000-10% discount,below 3000-no discount
"""
bill=float(input(" "))

if bill>5000:
  discount=bill*0.2

elif bill>=3000 and bill<=5000:
  discount=bill*0.1

else:
  discount=0

final_bill=bill-discount
print("Discount:",discount)
print("Final Bill: ",final_bill)
#wap to input four numbers from the user and find the greatest number among them
a=int(input(" "))
b=int(input(" "))
c=int(input(" "))
d=int(input(" "))
if(a>b and a>c and a>d):
  print("Greatest number: ",a)
elif(b>a and b>c and b>d):
  print("Greatest number: ",b)
elif(c>a and c>b and c>d):
  print("Greatest number: ",c)
else:
  print("Greatest Number: ",d)
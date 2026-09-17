#wap to input marks of 10 students. Store only valid marks between 0 and 100 in a list. Skip invalid marks.
marks=[]

for i in range(0,9):
  m=int(input("Enter marks of student "+ str(i) + ": "))
  if m>=0 and m<=100:
   marks.append(m)


print("Valid Marks: ",marks)
        
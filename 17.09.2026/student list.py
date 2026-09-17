#wap to input marks of n students in a list.Display highest marks,lowest marks, average marks, and a number of student who passed.
n=int(input("Number of students: "))
marks=[]
for i in range(n):
  m=int(input("Enter marks: "))
  marks.append(m)

highest=max(marks)
lowest=min(marks)
average=sum(marks)/n

passed=0

for m in marks:
  if m>=40:
    passed+=1

print("Highest Marks: ",highest)
print("Lowest Marks: ",lowest)
print("Average Marks: ",average)
print("Total number of student passed: ",passed)



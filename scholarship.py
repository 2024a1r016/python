"""wap to determine whether a student is eligible for a scolarship.
the scholarship should be granted if the student satisfies either of the following conditions:
a) The student has a CGPA of 8.5 or above and attendance of 85 percent or above.
b)The student has won a national level competition.
The program should take cgpa,attendance percentage,and national-level competition status as input,then display whether the student is eligible or not"""
cgpa=float(input("Enter CGPA: "))
per=int(input("Attendance Percentage: "))
status=input("National-level competition status: ")
if cgpa>=8.5 and per>=85 or status=="yes":print("Student is eligible for scholarship!")
else:print("Not Eligible:(")
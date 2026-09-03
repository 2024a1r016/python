#take student's full name and roll number.Generate email using first 3 letters of first name,first 3 letters of last name,and last 3 characters of roll number
fname=input(" ")
sname=input(" ")
roll=input(" ")
email=fname[:3]+sname[:3]+roll[-3:]
print(email)
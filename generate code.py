#Take name,branch,and year.Generate a code name using string contentation 
name=input(" ")
branch=input(" ")
year=input(" ")
code=name[:3]+"-"+branch[:3]+"-"+year[-2:]
print("*"*30)
print("Student_code: ",code)
print("*"*30)
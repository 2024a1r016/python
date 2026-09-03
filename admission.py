#Take roll number like 2024a1r016 and extract admission year,program code,and roll number digits using slicing.
roll=input(" ")
print("Admission Year: ",roll[:4])
print("Program code: ",roll[4:6])
print("Roll Number: ",roll[-2:])
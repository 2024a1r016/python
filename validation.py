"""WAP to create a simple password validation system.
The program should repeatedly ask the user to enter a password until a valid password is entered.A password will be considered valid only if it has at least 8 characters and contains the @ symbol.
once the user enters a valid password, the program should display "Password accepted." and stop.Otherwise, it should display "weak password" try again and ask for password again"""
while True:
  password=input("Enter your password: ")

  if len(password)>=8 and "@" in password:
    print("Password accepted")
    break
  else:
    print("Weak password. Try again later.")



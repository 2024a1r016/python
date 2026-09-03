"""wap to stimulate a digital lock system
The lock should ask the user to enter a 4-digit PIN. If the entered PIN does not contain exactly 4 digits, the program should display an error message and ask again. If the entered PIN is correct,the lock should open.Otherwise, the program should ask the user to try again"""
pin=input("Enter PIN: ")
if len(pin)!=4 and pin==1234 :print("Error,Try Again!")

else:print("Lock Open!")
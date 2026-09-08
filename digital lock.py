"""wap to stimulate a digital lock system
The lock should ask the user to enter a 4-digit PIN. If the entered PIN does not contain exactly 4 digits, the program should display an error message and ask again. If the entered PIN is correct,the lock should open.Otherwise, the program should ask the user to try again"""
correct_pin="1205"

while True:
    pin=input("Enter PIN: ")

    if len(pin) != 4:
        print("PIN must be exactly 4 digit,")
        continue

    if pin == correct_pin:
        print("Lock Opened!")
        break
    else:
        print("Error, Try Again!")
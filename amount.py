#wap to take an amount in rupees and calculate ho many rupees 500 and ruppees 100 notes are needed
total_money=int(input(" "))
big_note=total_money//500
rem=total_money%500
small_note=rem//100
print(f"{total_money}= {big_note} notes of 500 and {small_note} notes of 100")
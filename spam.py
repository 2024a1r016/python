#wap to detect whether a comment is spam or not. A comment should be treated as spam if it contains any of these keywords: "make a lot of money", "Buy now", "subscribe this", "Click this"
comment=input(" ")
if comment=="make a lot of money" or comment=="Buy now" or comment=="subscribe this" or comment=="Click this":
  print("Spam detected")
else:
  print("New message!!<3")
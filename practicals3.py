s = "welcome to python world"

print("Original string:", s)

count = 0

for ch in s:
    if ch.isalpha():
        count += 1

print("Number of alphabets:", count)

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
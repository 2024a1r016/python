#take an email address and print username,domain,reverse domain[yadvi@1806gmail.com]
email=input("Enter email address:")
index=email.find("@")
domain=email[index+1:]
reverse_domain=domain[::-1]
name=email[:index]
print("Username: ",name)
print("Domain: ",domain)

print("Reverse Domain: ",reverse_domain)
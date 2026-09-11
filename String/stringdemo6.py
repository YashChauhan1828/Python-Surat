name = input("Enter your name : ")
upper = ""
for i in name:
    if ord(i) >= 97 and ord(i) <= 122:
        upper += chr(ord(i)-32)
    else:
        upper += i

print(upper)        
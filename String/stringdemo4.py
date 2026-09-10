name = input("Enter your name")
char = input("Enter the character")
flag = -1

for i in range(len(name)):
    if name[i] == char:
        flag = i
        break

print("Character presesnt at",flag+1,"Position")   


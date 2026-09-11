name = input("Enter your name : ")
reverse = ""
# for i in range(len(name)-1,-1,-1):
#     reverse += name[i]

# print(reverse)

i = len(name)
while(i-1 > -1):
    reverse += name[i-1]
    i-=1

print(reverse)
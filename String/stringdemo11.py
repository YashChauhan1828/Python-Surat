name = input("Enter your name : ")
reverseName = ""

for i in range(len(name)-1,-1,-1):
    reverseName += name[i]

if(name == reverseName):
    print("String is palingdrome")
    
else:
    print("String is not palingdrome")
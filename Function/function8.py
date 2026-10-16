def commerce(name):
    print(f"{name} sceure addmission in commerce")
    return f"congratualtions {name}"

def science(name):
    print(f"{name} sceure addmission in Science")
    return f"congratualtions {name}"

def arts(name):
    print(f"{name} sceure addmission in arts")
    return f"congratualtions {name}"

def addmission(cb,name): # cd = science()
    print("Addmission secured")
    # cb(name)
    x = cb(name)
    print(x)

name = input("Enter student name: ")
marks = int(input("Enter your marks : "))
if marks > 80:
    addmission(science,name)
elif marks >70:
    addmission(commerce,name)
else:
    addmission(arts,name)
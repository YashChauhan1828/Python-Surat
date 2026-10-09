# 1)without argument and without return value

def greet(): # Function creation
    print("Hello , Good Morning")

greet() # function calling


# 2) with argument and without return value

def addition(a,b):
    c = a + b
    print(c)

addition("Hello", "World")

def addition1(a:int,b:int):
    c = a + b
    print(c)

addition1(10,20)

def addition2(a=10,b=20):
    c = a + b
    print(c)

addition2(50,60)
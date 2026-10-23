# def greet():
#     '''
#     Greet Function
#     '''
#     print("Hello Good Evening")

# greet()    

# def add(a:int,b:int):
#     print(a+b)

# add("a","b")

def description(name , age):
    a = 10 # Local Variable
    print("Name : ",name)
    print("Age : ",age)

# # description(22,"yash")
# description(age=22 , name="yash")

# def getstudents(**kwargs):

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# getstudents(rollno=101, name="raj", marks=90)

# def getstudents(*args):
#     for student in args:
#         print(student)

# getstudents("raj","johnny","mukesh","sara")


# b = 20 # global Variable
# def description(name , age):
#     a = 10 # Local Variable
#     print("Name : ",name)
#     print("Age : ",age)
#     print("a : " ,a)
#     print("b : " ,b)

# description("yash",22)

def average(*args):
    for marks in args:
        avg  = sum(args)/len(args)
        return avg

data = average(10,20,30,40,50)
print(data)


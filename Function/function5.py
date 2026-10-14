# def getstudents(x,y,*args):
#     for student in args:
#         print(student)
#     print(f"First student is: {x}")
#     print(f"Second student is: {y}")

# getstudents("raj","john")
# getstudents("raj","john","mike","sara")


def getstudents(*args , x):
    for student in args:
        print(student)
    print(x)

getstudents("raj","john","mike","sara",x="Yash")
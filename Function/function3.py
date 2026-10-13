def getstudents(*args):
    for student in args:
        print(student)

getstudents("raj","john","mike","sara")


def getstudents(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

getstudents(rollno=101, name = "raj" , marks = 90)
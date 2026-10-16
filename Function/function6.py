def getstudents(*args):
    for i in args:
        print(type(i).__name__)

getstudents(10,20,30,40,50)
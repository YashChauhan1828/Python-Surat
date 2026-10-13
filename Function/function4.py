def getstudents(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

getstudents(rollno=101, name="raj", marks=90)
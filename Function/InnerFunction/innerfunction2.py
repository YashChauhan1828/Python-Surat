def login_system(username,password):

    def validate_user():

        return username == "ADMIN" and password == "ADMIN"

    valid = validate_user()
    if (valid) :
        print("Login Sucessful")

    else:
        print("Login not Sucessful")

username = input("Enter username : ")
password = input("Enter password : ")
login_system(username,password)
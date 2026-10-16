# Higher Order Function

def tobecalled():
    print("Function is called")

def calling(a):
    print("Function is running")
    a()

calling(tobecalled) # calling a another function as argument
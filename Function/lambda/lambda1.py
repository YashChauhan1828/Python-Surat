# We can't use loops and elif keywords in the lambda function.

# def abc(x):
#     print(x)

# abc(100)

test1 = lambda x : print(x)
test1(100)

test2 = lambda x, y : x+y 
print(test2(10,20))

test3 = lambda age : "Eligible for voting" if age >= 18 else "not eligible for voting"
print(test3(20))

test4 = lambda num: "Positive" if num > 0 else ("neg" if num < 0 else "zero")
# print(test4(5))
print(test4(5.22))
import random

# value1 = random.random() # print 0 to 1 random float value
# print(value1)

# value2 = random.randint(1, 100) # print random integer value between 1 to 100 including both 1 and 100
# print(value2)

# value3 = random.uniform(1 ,100) # print random float value between 1 to 100 including both 1 and 100
# print(value3)

# value4 = random.randrange(1 , 100 , 3) # print random integer value between 1 to 100 including 1 but excluding 100 and the step is 3
# print(value4)

# value5 = random.choice(('a','b','c','d')) # print random value from the given tuple/ list / dictionary / 
# print(value5)

# value6 = random.choice((1,'b',5,'d' , "Yash")) # print random value from the given tuple/ list / dictionary / 
# print(value6)

data = [1,2,3,4,5]
value7 = random.shuffle(data) # provides random shuffling of the given list/tuple/dictionary/string
print(data)
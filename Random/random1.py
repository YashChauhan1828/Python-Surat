import random

value = random.random() # 0 to 1
print(value)

value3 = random.randint(1 , 100) # provides random integer between 1 to 100 including both 1 and 100
print(value3)

value2 = random.randrange(1, 100 , 3) # provides random integer between 1 to 100 including 1 but excluding 100 and the step is 3 
print(value2)

value4 = random.uniform(1 , 100) # provids random float between 1 to 100 including both 1 and 100.
print(value4)

value5 = random.choice((1,2,3,4,5)) # provides random value from the given tuple/ list / dictionary / string
print(value5)

value6 = random.choice(list({"Name" : "John", "Age" : 25, "City" : "New York"})) # provides random value from the given tuple/ list / dictionary / string
print(value6)

data = [1,2,3,4,5]
random.shuffle(data) # provides random shuffling of the given list
print(data)

# print(random.shuffle([1,2,3,4,5])) 

random.seed(10) # provides same random value for the given seed value
print(random.random())
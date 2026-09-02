import random

# random function:
print(random.random()) # provides random float value between 0 to 1 

# random integer function:
print(random.randint(1, 100)) # provides random integer between 1 to 100 including both 1 and 100

# uniform function:
print(random.uniform(1, 100)) # provides random float between 1 to 100 including both 1 and 100

# randrange function:
print(random.randrange(1, 100, 3)) # provides random integer between 1 to 100 including 1 but excluding 100 and the step is 
# 1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97

print(random.randrange(-10 , 10))

# choice function:
print(random.choice((1,2,3,4,5))) # provides random value from the given tuple/ list / dictionary / string

# shuffle function:
data = [1,2,3,4,5]
random.shuffle(data)
print(data)

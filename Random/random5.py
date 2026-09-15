import random

# random()
print(random.random()) # # Print a random float between 0.0 and 1.0

# randint()
print(random.randint(1,100)) # Print a random integer between 1 and 100 (inclusive)

# uniform()
print(random.uniform(1,100)) # Print a random float between 1 and 10

# randrange()
print(random.randrange(1,100,3)) # Print a random integer from the range 1 to 10 with a step of 3

# choice()
print(random.choice([1,2,3,4,5]))
print(random.choice([1,4.65,"yash",True]))

# shuffle()
# print(random.shuffle([1,2,3,4,5]))
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
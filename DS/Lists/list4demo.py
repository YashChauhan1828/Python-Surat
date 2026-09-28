data = ["ram","shyam","amit","kunal","ajay"]
print(data)

data.pop()  # If index is not given then removes data from the last. 
print(data)

data.pop(2) # If index is provided then data gets remove from the specific index.
print(data)

data.pop(-3)
print(data)

data.pop(-4) # Index out of range error.
print(data)
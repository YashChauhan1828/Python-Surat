data = ["ram","shyam","amit","kunal","ajay","kunal","kunal","yash"]
# print(data)

print(data.index("kunal"))
print(data.count("yash"))

data.reverse()
print(data)

data.sort() # By default sorts in ascending order.
print(data)

data.sort(reverse=True) # Sorts the list in decending order
print(data)

data.sort(key=len)
print(data)

data.sort(key = len , reverse= True)
print(data)


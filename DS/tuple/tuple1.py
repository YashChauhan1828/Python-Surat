tuple1 = (1,2,3,4,5,6,7,7,8)
print(type(tuple1))
print(tuple1)

# tuple1[5] = 9
# print(tuple1)

print(tuple1.__add__((4,5,6,"Yash",4.87)))
print(tuple1.count(0))
print(tuple1.index(5))

list1 = list(tuple1)
print(list1)

print(tuple1[0:6])
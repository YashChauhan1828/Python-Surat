lst1 = [1,2,4,5]
print(type(lst1)) 

lst2 = [1,True,4.6,"Yash"]
print(type(lst2))

lst3 = [1,2,3,4,5]
print(lst3)  # Representation of list.

print(lst3[0])
lst3[-1] = 6
print(lst3)

lst3[4] = 7
print(lst3)

for i in lst3:
    print(i,end="")
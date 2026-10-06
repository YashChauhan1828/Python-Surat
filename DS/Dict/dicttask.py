data = {1:100,2:34,3:23,4:121,5:44}
lst = []

for i,j in data.items():
    if j%2==0:
        lst.append(i)
print(lst)

# print(data.items())
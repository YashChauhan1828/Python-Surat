set1 = {1,2,3,4,5,5,6,7,8,2,2,2,2,2,1,1,"Rudra", "Snehil" , "OM" , 6.75 , "TEJAS" , 5.43 , "TIRTH"}
print(set1)
# print(set1[6])

set1.add("Yash")
print(set1)

set1.update(["Pooja" , "krinal"])
print(set1)

set1.update({99,100,212121})
print(set1)

set1.remove("OM")
print(set1)

set1.remove("Snehil")
print(set1)

set1.pop()
print(set1)

set1.discard("TEJAS")
print(set1)
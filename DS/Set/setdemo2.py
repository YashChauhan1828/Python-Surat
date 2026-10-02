user1 = {"ram","shyam","amit","sumit","ajay"}
user2 = {"ram","shyam","amit","kunal","parth"}

# print(user1.union(user2))
# print(user1.intersection(user2))
# print(user1.difference(user2))
print(user1.symmetric_difference(user2))
# print(user1.difference_update(user2))
print(user1.isdisjoint(user2))
print(user1.issubset(user2))
print(user1.issuperset(user2))
name = input("Enter your name : ")

print(len(name))

print(len(name.strip("a")))
print(len(name.lstrip()))
print(len(name.rstrip()))


print(name.swapcase())

print(name.startswith(("y","a","s","h")))
print(name.endswith(("h","s","u")))

print(name.isalnum())
print(name.isalpha())
print(name.isdigit())
print(name.islower())
print(name.isupper())
print("isSpace",name.isspace())
print("title",name.istitle())
print("isPrintable",name.isprintable())

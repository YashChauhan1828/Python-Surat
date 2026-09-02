import math
a = 1
b = 8
c = 16

discriminant = (b ** 2) - (4 * a * c)
print("Discriminant is : ",discriminant)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("the roots are : ",root1 , "and ", root2)

elif discriminant == 0:
    root = -b/(2 * a)
    print("the root is : ",root)

else:
    print("the roots are imaginary")

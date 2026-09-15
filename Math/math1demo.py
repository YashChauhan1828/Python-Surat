import math

a = 15
# Square root
print("Square root : ",math.sqrt(a))

# power
print("Power : ",math.pow(a,6))

# Factorial
print("Factorial : ",math.factorial(15))

# Ceil value
print("Ceil value for positive: ",math.ceil(3.0000000001))
print("ceil value for negative: ",math.ceil(-4.358))


# Floor Value
print("Floor Value: ",math.floor(3.222222))
print("floor value for negative: ",math.floor(-6.821))

# absolute value
print("Absolute Value: ",math.fabs(-7.842))
print("Absolute Value: ",math.fabs(7.842))

# logithmic value
print("Logarithmic value: ",math.log(100)) 
print("Logarithmic value: ",math.log(100,10)) 

# Exponential Value
print("Exponential Value: ",math.exp(7))

# GCD/HCF
print("GCD is: ",math.gcd(12,15))
print("GCD is: ",math.gcd(19,15))

# LCM
print("LCM is : ",math.lcm(12,15))

# # Trigonometric Functions

print("Sine Value: ",math.sin(math.radians(0)))
print("Cosine value: ",math.cos(math.radians(0)))
print("Tangent Value: ",math.tan(math.radians(90)))
print("Cosecant Value : ",1 / (math.sin(math.radians(30))))
print("Secant Value : ",1 / (math.cos(math.radians(60))))
print("Cotangent Value : ",1 / (math.tan(math.radians(45))))

# # constant
print("Value of pi: ",math.pi)
print("Value of e: ",math.e)

# modf
print(math.modf(5.75))
print(math.modf(-6.85))

# permutations
print("Permutations: ",math.perm(5,3))

# combinations
print("Combinations: ",math.comb(5,3))


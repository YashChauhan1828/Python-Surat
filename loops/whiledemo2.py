ORIGINAL_NUMER = int(input("Enter a number: "))
total_digits = 0
sum = 0
temp = ORIGINAL_NUMER
temp2 = temp

while(ORIGINAL_NUMER > 0):
    ORIGINAL_NUMER = ORIGINAL_NUMER // 10
    total_digits += 1

while(temp > 0):
    digit = temp % 10
    sum += (digit ** total_digits)
    temp = temp // 10

if (sum == temp2):
    print("Number is Armstrong number")
else:
    print("Number is not Armstrong number")
no = 153
sum = 0

for i in str(no):
    sum += int(i) ** len(str(no))

if no == sum :
    print("Number is armstrong")
else:
    print("Number is not armstrong")
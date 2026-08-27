marks = int(input("Enter your marks: "))
print("Your marks are: ", marks)

if marks >= 95 and marks <= 100:
    print("Grade A")
    
elif marks >= 80 and marks < 95:
    print("Grade B")
    if marks >= 85:
        print("Very Good")

elif marks >= 70:
    print("Grade C")

else:
    print("fail")



marks = int(input("Enter your marks: ")) - 1 
print("Your marks are: ", marks)

if marks >= 90:
    print("Grade A")
    if marks >= 95:
        print("Excellent")

elif marks >= 80:
    print("Grade B")
    if marks >= 85:
        print("Very Good")

elif marks >= 70:
    print("Grade C")

else:
    print("fail")



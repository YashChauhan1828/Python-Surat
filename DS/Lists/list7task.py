# please entrt y for continue and 'n' for exit
# y
# enter movie name:
# enter relese year:

# please entrt y for continue and 'n' for exit
# n

# [["chava",2025],["abc",2050],[]]


movieData = []
while True:
    choice = input("Press y for continue and n for break").strip()
    if (choice == 'y'):
        movieName = input("Enter movie name : ").strip()
        releaseYear = int(input("Enter release Year : "))
        data = [movieName,releaseYear]
        movieData.append(data)

    elif (choice == 'n'):
        break

    else : 
        print("Invalid choice")
        break

print(movieData)

def outerfunction(): # External Function
    print("Outer Function Called")

    def innerfunction(): # Inner Function
        print("Inner Function Called")

    innerfunction()

outerfunction()

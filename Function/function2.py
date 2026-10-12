# 3) with argument and with return value

def addition3(a:int , b:int) -> int:
    return a + b

def main():
    c = addition3(10,20)
    print(c)

if __name__ == "__main__":
    main()

# 4) without argument and with return value

def addition() -> int:
    a=10
    b=20
    return a + b

def main():
    c = addition()
    print(c)

if __name__ == "__main__":
    main()
    # addition()


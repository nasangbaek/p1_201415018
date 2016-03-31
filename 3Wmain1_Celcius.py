def print_options():
    print("option:")
    print(" 'P' print option")
    print(" 'C' C2F")
    print(" 'F' F2C")
    print(" 'E' exit")

def C2F(x):
    return 9.0 / 5.0 * x + 32

def F2C(y):
    return (y- 32.0) * 5.0 / 9.0

choice = "P"
while choice != "E":
    if choice == "C":
        x = float(input("섭씨 온도: "))
        print("화씨 온도:", C2F(x))
        choice = input("option: ")
    elif choice == "F":
        y = float(input("화씨 온도: "))
        print("섭씨 온도:", F2C(y))
        choice = input("option: ")
    elif choice == "P":
        print_options()
        choice = input("option: ")
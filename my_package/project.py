def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

while True:
    print("1.Addition\t2.Substraction\n3.multiply\t4.divide")
    ch=int(input("Enter your Choice"))
    match ch:
        case 1:
            print(add(5,6))
        case 2:
            print(subtract(6,3))
        case 3:
            print(multiply(3,3))
        case 4:
            print(divide(3,3))
        case _:
            print("Invalid Choice")
            break
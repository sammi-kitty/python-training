#!/usr/bin/python3

def main():

    op = input("Ange operator (+, - ,*, /):")
    value1 = float(input("Ange första värdet:"))
    value2 = float(input("Ange andra värdet:"))

    if (op == "+"):
        result = value1 + value2
    elif (op == "-"):
        result = value1 - value2
    elif (op == "*"):
        result = value1 * value2
    elif (op == "/"):
        result = value1 / value2

    print("Värdet av " + str(value1) + op + str(value2) + "=" + str(result))

main()
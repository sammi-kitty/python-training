#!/usr/bin/python3

def main():
    value1 = input("Value 1: ")
    value2 = input("Value 2: ")
    value3 = input("Value 3: ")

    smallest_value = float(value1)

    if (float(value2) < smallest_value):
        smallest_value = float(value2)

        if (float(value3) < smallest_value):
            smallest_value = float(value3)
    
    print(smallest_value)

main()
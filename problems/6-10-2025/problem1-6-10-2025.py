#!/usr/bin/python3

def main(): 

    max_value = input("Vilket tal vill du räkna till?")
    max_value = int(max_value)

    i = 2
    while i <= max_value:
        print(i)
        i = i + 2

main()
#!/usr/bin/python3

def main():

    max_value = int(input("Skriv in det tal du vill räkna till: "))

    sum = 0
    i = 2
    while i <= max_value:
        sum = sum + i
        print(i, sum)

        i = i + 2

main()
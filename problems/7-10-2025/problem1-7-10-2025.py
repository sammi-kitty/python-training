#!/usr/bin/dev

# Problem: Find all occurences of the substring part in the string whole
# Solution: use the whole.find() function to check and count substrings
# Make sure to keep track of current index to continue searching through the string

def main():
    whole = input("Input the entire string: ")
    part = input("Input the partial string you want to search for: ")

    count = 0
    index = whole.find(part)
    while index != -1:
        print(index)
        count = count + 1

        index = whole.find(part, index + 1)
    
    print(part, "was found", count, "times in", whole)

main()
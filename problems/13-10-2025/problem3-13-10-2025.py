#!/usr/bin/python3

def main():
    year = int_input("Enter a year: ")

    if is_leap_year(year):   
        print("The year", year, "is a leap year") 
    else:  
        print("The year", year, "is a common year")

def int_input(text):
    answer = ""
    while answer.strip() == "" or not answer.isdigit():
        answer = input(text)
        
        if not answer.isdigit():
            print("Not an integer")

    return int(answer)

def is_leap_year(year):
    isleap = False

    if year % 400 == 0:
        isleap = True
    elif year % 100 == 0:
        isleap = False
    elif year % 4 == 0:
        isleap = True

    return isleap

main()
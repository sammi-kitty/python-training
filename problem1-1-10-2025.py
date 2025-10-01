#!/usr/bin/python3

import datetime

def main():
    answer = str("")
    while (is_integer(answer) == False):
        answer = input("Vilket år är du född?\n")

        if (is_integer(answer) == False):
            print("Det där är inte ett heltal, försök igen.")

    print("Du är född år: " + answer)
    print("Du är "
          + str(int(datetime.datetime.now().year) - int(answer)) 
          + " år gammal")

def is_integer(value):
    try:
        int(value)
        return True
    
    except:
        return False
    
main()
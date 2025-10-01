#!/usr/bin/python3
import datetime

# Problemformulering: 
# 1. Fråga användaren vilket år hen är född.
# 2. Skriv ut året samt hur gammal användaren är.
#
# Not: Användaren kan skriva in något annat än ett heltal, därmed:
# (3. Tvätta input).

def main():
    answer = str("")

    # Om svaret INTE är en integer vill vi ställa frågan igen.
    while (is_integer(answer) == False):
        answer = input("Vilket år är du född?\n")

        if (is_integer(answer) == False):
            print("Det där är inte ett heltal, försök igen.")

    # Output print statements.
    print("Du är född år: " + answer)
    print("Du är "
          + str(int(datetime.datetime.now().year) - int(answer)) 
          + " år gammal")

# Funktion som ser om value är ett heltal eller inte.
def is_integer(value):
    try:
        int(value)
        return True
    
    except:
        return False
    
main()
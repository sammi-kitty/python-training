#!/usr/bin/python3

def main():

    answer = input("Skriv en sekvens av heltal separerade med ett mellanslag: ")

    list = answer.split()

    sum = 0
    for i in range(0, len(list), 2):
        sum = sum + int(list[i])
    
    print("Summan av vartannat tal är: " + str(sum))

main()
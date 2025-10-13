#!/usr/bin/python3

def main():
    value = input("promptstr: ")
    response = read_input_from_user(value)

    print(response)

def read_input_from_user(promptstr):

    cmd = ""
    while cmd.strip() == "":
        cmd = input(promptstr)

    return cmd

main()
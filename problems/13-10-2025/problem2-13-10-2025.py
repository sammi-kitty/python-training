#!/usr/bin/python3

def main():
    value = input("write something ")
    response = read_input_from_user(value)
    print(response)

def read_input_from_user(promptstr):

    cmd = ""
    while cmd.strip() == "" or (int_input(cmd) == False):
        cmd = input(promptstr)

    return cmd

def int_input(text):
    # Check if text is only digits (UNNECESSARY FUNCTION STATEMENT)

    if text.isdigit():
        return True
    else:
        return False

main()
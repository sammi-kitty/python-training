def main():
    print("Welcome to PyCalculator")
    loop = True
    while loop == True:
        print_menu()

        choice = option_picker(["1", "2", "3", "4", "5"])
        if choice == 1:
            add()

        elif choice == 2:
            subtract()

        elif choice == 3:
            multiply()

        elif choice == 4:
            divide()

        elif choice == 5:
            loop = False
        print()

    print("Thank you for using PyCalculator!")

def add():
    '''Ask user for 2 floats and add them'''

    op1 = float_input("Add this: ")
    op2 = float_input("to this: ")
    print("{:.2f} + {:.2f} = {:.2f}".format(op1, op2, op1 + op2))

def subtract():
    '''Ask user for 2 floats and subtract them'''

    op1 = float_input("Subtract this: ")
    op2 = float_input("from this: ")
    print("{:.2f} - {:.2f} = {:.2f}".format(op1, op2, op1 - op2))

def multiply():
    '''Ask user for 2 floats and multiply them'''

    op1 = float_input("Multiply this: ")
    op2 = float_input("with this: ")
    print("{:.2f} * {:.2f} = {:.2f}".format(op1, op2, op1 * op2))

def divide():
    '''Ask user for 2 floats and divide them'''

    op1 = float_input("Divide this: ")
    op2 = float_input("by this: ")
    print("{:.2f} / {:.2f} = {:.2f}".format(op1, op2, op1 / op2))

def float_input(text):
    '''Ask the user for an input with param:text and make sure the response is a float'''
    answer = ""
    while not is_float(answer):
        answer = input(text)
    
    return float(answer)

def option_picker(valid_answers):
    '''Make the user pick a value from a set of values'''

    answer = ""
    while not answer in valid_answers:
        answer = input("Choose your option: ")

    return int(answer)

def is_float(value):
    '''Check if a value is a float'''

    try:
        float(value)
        return True
    except: 
        return False

def print_menu():
    '''Print the pycalculator menu'''

    print("Your options are:")
    print()
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator.py")
    print()

main()
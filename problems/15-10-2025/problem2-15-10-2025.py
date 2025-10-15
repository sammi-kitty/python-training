import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__))

def main():
    file_path = os.path.join(PROJECT_DIR, "vampire_bat_mRNA-1.dat")

    data = []
    with open(file_path, "r") as file:
        for row in file.readlines():
            if row[0] == "#":
                pass
            else:
                fixed_row = format_string(row)
                print(fixed_row)
                data.append(fixed_row)
    
    new_file("".join(data), "batrna.txt")

def new_file(to_print, filename):
    # Write to_print to new or existing file filename in current dir

    file_path = os.path.join(PROJECT_DIR, filename)
    with open(file_path, "w") as file:
        file.write(to_print)

file_path = os.path.join(PROJECT_DIR, "vampire_bat_mRNA-1.dat")

def format_string(string):
    # Takes a string, 
    # splits it, 
    # removes the first element 
    # and puts it back together without spaces

    split_string = string.split()
    split_string.pop(0)
    # Alternativt: del split_row[0]
    formatted_string = "".join(split_string)

    return formatted_string

main()
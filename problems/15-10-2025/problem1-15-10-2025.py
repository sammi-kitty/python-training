#!/usr/bin/python3
import os

def PROJECT_DIRECTORY(): 
    return os.path.join(os.path.dirname(__file__))

def FILE_PATH(): 
    return os.path.join(PROJECT_DIRECTORY(), "dates.txt")

def main():
    print(FILE_PATH())

    dates = []
    with open(FILE_PATH(), "r") as file:
        for row in file.readlines():
            end_index = row.find(" ")
            data = {
                "date": row[:end_index],
                "name": row[end_index:].strip()
            }
            dates.append(data)

    born_in_1st_half = []
    born_in_2nd_half = []
    for date in dates:
        if int(date["date"][5:6]) >= 7:
            born_in_2nd_half.append(date)
        else:
            born_in_1st_half.append(date)

    print(born_in_1st_half, born_in_2nd_half)

main()
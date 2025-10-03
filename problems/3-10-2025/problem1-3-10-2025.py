#!/usr/bin/python3
import random

PROBABILITIES = ["1","x","2"]

# Problemformulering:
# Generera tips om 13 rader (1,X,2)
# Sluta när användaren säger till
# Bonus: Sannolikheten för de olika värdena ska vara ändringsbar

def main():

    tips = []
    while True:
        list = []

        # Skapa 1 tipsrad
        for i in range(13):
            list = list + [PROBABILITIES[random.randint(0, len(PROBABILITIES) - 1)]]

        # Addera tipsraden till de andra tipsraderna
        tips = tips + [list]
        print (tips)

        # Fråga användaren om vi vill gå vidare
        cmd = input("Continue? Y/N")
        if (cmd.lower() != "y"):
            break

main()
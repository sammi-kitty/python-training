#!/usr/bin/python3
import random

from modules.words import get_words

def main():
    print("Wordle!")

    available_words = get_words()
    word = available_words[random.randint(0, len(available_words) - 1)]

    

main()
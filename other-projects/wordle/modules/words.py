import os

WORDS_PATH = os.path.join(os.path.dirname(__file__), "words.txt")

def get_words():

    words = []
    with open(WORDS_PATH) as file:
        for line in file:
            words.append(line.strip())
    
    return words
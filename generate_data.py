import os
import random
from random_word import RandomWords
import time

r = RandomWords()
FILE = r"test2.txt"

fo = open(FILE, "w+")

words = [
    "alonso",
    "perro",
    "gato",
    "mascota",
    "pepe",
    "monica",
    "loro",
    "anastasia",
    "melanie",
    "pavlov",
    "amnesia",
    "interesante",
    "picante",
    "tapir",
    "valdivia",
    "cloud",
    "computer",
    "science",
]


def get_size():
    return os.path.getsize(FILE)


# 1 MB = 1e6 bytes


def create_words(n_words):
    global words
    i = 0
    while i < n_words:
        word = r.get_random_word()
        if word is not None:
            words.append(word)
            i += 1
    words.append("\n")


MB = 1000000


def main():
    create_words(10)
    print(words)
    inicio = time.time()
    while get_size() < (500* MB):
        r = random.randint(0, len(words) - 1)
        if r == len(words) - 1:
            fo.write(words[r])
        else:
            fo.write(words[r] + " ")
    fin = time.time()
    print(fin - inicio)  # 1.0005340576171875
    fo.close()
    print("File " + fo.name + " ready! with:", get_size() / MB, "MB")


main()

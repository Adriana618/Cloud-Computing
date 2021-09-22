from pathlib import Path
import os
import logging
import threading
import time
import concurrent.futures

FILE = r"test2.txt"

FILEG = os.open(FILE,os.O_RDWR)
blocking = False
os.set_blocking(FILEG, blocking)
os.close(FILEG)
num_threads = 1

words = {}

offset_list = []

offset = 0

lock = threading.Lock()

def get_words(line):
    global words
    _words = line.split(" ")
    print(_words)
    for _word in _words:
        words[_word] += 1
    print("xxxx", words, "----")


def thread_function(my_offset):
    global offset
    words_local = {}
    MY_FILE = open(FILE, "r")
    perfect = False
    ##validate##
    if my_offset != 0:
        MY_FILE.seek(my_offset - 1)
        line = [MY_FILE.readline()]
        if line == "\n":
            perfect = True
    ############
    MY_FILE.seek(my_offset)
    if not perfect:
        MY_FILE.readline()
    while MY_FILE.tell() < (my_offset + offset):
        line = MY_FILE.readline().strip("\n")
        if not line:
            pass
        global words
        _words = line.split(" ")
        for _word in _words:
            if words_local.get(_word, False):
                words_local[_word] += 1
            else:
                words_local[_word] = 1
    with lock:
        for key,val in words_local.items():
            if words.get(key,False):
                words[key] += val
            else:
                words[key] = val


def get_size():
    return os.path.getsize(FILE)


def fill_offset(my_offset):
    global offset_list
    for i in range(0, get_size(), my_offset):
        offset_list.append(i)


def main():
    global offset
    offset = get_size() / num_threads
    fill_offset(int(offset + 1))
    print(offset_list)
    inicio = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(thread_function, offset_list)
    fin = time.time()
    print(fin - inicio)  # 1.0005340576171875
    print(words)


if __name__ == "__main__":
    main()
# print(get_size())

# fo = open(FILE, "r+")

# fo.seek(11)

# line = [fo.readline()]

# print("---",line,"---")
# print(fo.tell())

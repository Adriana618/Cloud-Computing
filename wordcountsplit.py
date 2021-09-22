from pathlib import Path
import os
import logging
import threading
import time
import concurrent.futures

FILE = ["test1.txt","test2.txt","test3.txt","test4.txt"]

num_threads = 4

words = {}

offset_list = []

offset = 0

lock = threading.Lock()


def get_size(_FILE):
    return os.path.getsize(_FILE)

def thread_function(my_file):
    words_local = {}
    MY_FILE = open(my_file, "r")

    while MY_FILE.tell() < get_size(my_file):
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
        
    for key,val in words_local.items():
        if words.get(key,False):
            words[key] += val
        else:
            words[key] = val
    print("Terminado")



def main():

    inicio = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(thread_function, FILE)
    fin = time.time()
    print(fin - inicio)  # 1.0005340576171875
    print(words)


if __name__ == "__main__":
    main()
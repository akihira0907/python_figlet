#!/usr/bin/python3
# coding: UTF-8

import subprocess
import time

def main():
    f = open("sample.txt")
    sentences = f.read()
    f.close()
    words = sentences.split()
    
    for word in words:
        # print(word)
        subprocess.run(["figlet", word])
        time.sleep(0.1)
        subprocess.run(["clear"])

if __name__ == "__main__":
    main()


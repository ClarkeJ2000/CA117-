#!/usr/bin/env python3

import sys
import string

def count(s):
    total = 0
    seen = []
    for i in s:
        details = i.split()
        for word in details:
            word = word.lower()
            for c in word:
                if c in string.punctuation:
                    word = word.replace(c, '')
            if word not in seen:
                seen.append(word)
    return len(seen) - 1

def main():
    line = sys.stdin.readlines()
    print(count(line))
if __name__ == '__main__':
    main()

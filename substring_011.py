#!/usr/bin/env python3

import sys

def substring(s):
    word = s.substring()
    return True

def main():
    for line in sys.stdin.readlines():
        line = line.lower()
        line = line.strip().split()
        if line[0] in line[1]:
            print('True')
        else:
            print('False')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys

def count(s):
    total = 0
    for i in s:
        details = i.split()
        total = total + len(details)
    return total

def main():
    line = sys.stdin.readlines()
    print(count(line))
if __name__ == '__main__':
    main()

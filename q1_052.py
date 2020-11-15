#!/usr/bin/env python3

import sys

def swap(s, num):
   num = num * -1
   t = s[num:] + s[:num]
   return t

def main():
   string = sys.argv[1]
   n = int(sys.argv[2])
   num = n % len(string)
   print(rotate(string, num))

if __name__ == '__main__':
   main()

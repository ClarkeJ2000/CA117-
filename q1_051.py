#!/usr/bin/env python3

import sys

file = sys.argv[1]
file = list(file)

def swap(s):
	for i in range(0, len(file) - 1, 2):
		file[i], file[i + 1] = file[i + 1], file[i]
	print(''.join(file))

def main():
	swap(sys.argv[1])

if __name__ == '__main__':
	main()

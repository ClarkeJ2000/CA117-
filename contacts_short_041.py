#!/usr/bin/env python3

import sys

d = {}
with open(sys.argv[1], "r") as fd:
    lines = fd.readlines()
    for line in lines:
        line = line.split()
        d[line[0].strip()] = line[1].strip()

lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    if line not in d:
        print("Name:", line)
        print("No such contact")
    else:
        print("Name:", line)
        print("Phone:", d[line.strip()])

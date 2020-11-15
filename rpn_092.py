#!/usr/bin/env python3

from math import sqrt
from stack_092 import Stack

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


def negate(x):
    return -x

b = {'+': add, '-': subtract, '*': multiply, '/': divide}
u = {'n': negate, 'r': sqrt}

class calculator(line):
	stack = Stack()
	for e in line.split():
		if e in b.keys():
			y = stack.pop()
			x = stack.pop()
			stack.push(b[e](x, y))
		elif e in u.keys():
			stack.push(u[e](stack.pop()))
		else:
			stack.push(float(e))
	return stack.top()

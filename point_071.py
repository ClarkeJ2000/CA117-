#!/usr/bin/env python3

from math import sqrt
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = -self.x
        self.y = -self.y

    def distance(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

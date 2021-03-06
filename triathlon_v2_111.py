#!/usr/bin/env python3


class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(object):

    def __init__(self):
        self.mapping = {}

    def __str__(self):
        l = []
        for e in sorted(self.mapping.values(), key=lambda s: s.name):
            l.append("Name: {:s}".format(e.name))
            l.append("ID: {:d}".format(e.tid))
        return "\n".join(l)

    def add(self, triathlete):
        self.mapping[triathlete.tid] = triathlete

    def remove(self, tid):
        del self.mapping[tid]

    def lookup(self, tid):
        if tid in self.mapping:
            return self.mapping[tid]
        return None

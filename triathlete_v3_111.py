#!/usr/bin/env python3

class Triathlete:

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_time = 0

    def add_time(self, discipline, time):
        self.times[discipline] = time
        self.race_time += time

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.race_time)

    def __eq__(self, other):
        return self.race_time == other.race_time

    def __gt__(self, other):
        return self.race_time > other.race_time

    def __lt__(self, other):
        return self.race_time < other.race_time

    def get_time(self, discipline):
        return self.times[discipline]

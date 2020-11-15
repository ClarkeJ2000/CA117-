#!/usr/bin/env python3

class Employee(object):

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def wages(self):
        return 0

    def __str__(self):
       return 'Name: {}\nNumber: {}\nWages: {:.2f}'.format(self.name, self.number, self.wages())

class Manager(Employee):

    def __init__(self, name, number, salary):
        self.name = name
        self.number = number
        self.salary = salary

    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):

    def __init__(self, name, number, rate, hours):
        self.name = name
        self.number = number
        self.rate = rate
        self.hours = hours

    def wages(self):
        return self.rate * self.hours

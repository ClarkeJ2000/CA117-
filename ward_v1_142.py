#!/usr/bin/env python3

class Patient:

    def __init__(self, name, age, doctor):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __str__(self):
        return "Name: {}\nAge: {}\nDoctor: {}".format(self.name, self.age, self.doctor)

class Ward:

    def __init__(self):
        self.mapping = {}

    def add(self, patient):
        self.mapping[patient.name] = patient

    def remove(self, name):
        del self.mapping[name]

    def lookup(self, name):
        if name in self.mapping:
            return self.mapping[name]
        return None

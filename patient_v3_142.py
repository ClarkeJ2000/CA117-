#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, medication=()):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.members = list(medication)

    def add_medication(self, meds):
        self.members.append(meds)

    def __str__(self):
        return "Name: {}\nAge: {}\nMedications: {}\nDoctor: {}".format(self.name, self.age, ', '.join(self.members), self.doctor)

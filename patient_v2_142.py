#!/usr/bin/env python3

class Patient:

    def __init__(self, name, age, medication, doctor):
        self.name = name
        self.age = age
        self.medication = medication
        self.doctor = doctor

    def __str__(self):
        return "Name: {}\nAge: {}\nMedications: {}\nDoctor: {}".format(self.name, self.age, ', '.join(self.doctor), self.medication)

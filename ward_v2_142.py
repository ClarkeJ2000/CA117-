#!/usr/bin/env python3

class Patient:

    def __init__(self, name, age, medication, doctor):
        self.name = name
        self.age = age
        self.medication = medication
        self.doctor = doctor

    def __str__(self):
        return "Name: {}\nAge: {}\nMedications: {}\nDoctor: {}".format(self.name, self.age, ', '.join(self.doctor), self.medication)

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

    def get_patients_by_medication(self, medication):
            if self in medication:
                return self
            else:
                pass

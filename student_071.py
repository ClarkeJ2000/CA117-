#!/usr/bin/env python3
class Student():

    def __init__(self, surname, forename, sid, modlist=[]):
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, module):
        self.modlist.append(module)

    def del_module(self, module):
        try:
            self.modlist.remove(module)
        except ValueError:
            pass

    def print_details(self):
        print('ID: {}'.format(self.sid))
        print('Surname: {}'.format(self.surname))
        print('Forename: {}'.format(self.forename))
        print('Modules: {:s}'.format(' '.join(self.modlist)))

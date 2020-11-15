#!/usr/bin/env python3
from datetime import datetime
current_year = datetime.now().year

class Vehicle(object):
	def __init__(self, make, model, year, cost, miles, driver):
		self.make = make
		self.model = model
		self.year = year
		self.cost = cost
		self.miles = miles
		self.driver = driver

	def value(self):
		age = current_year - self.year
		return round(self.cost * (1 + self.d_rate)**age)

	def service(self):
		return self.srv_miles - self.miles % self.srv_miles

class Car(Vehicle):
	srv_miles = 10000
	d_rate = -0.1

class Motorcycle(Vehicle):
	srv_miles = 5000
	d_rate = -0.15
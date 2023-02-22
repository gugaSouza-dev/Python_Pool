from beverages import *
import random

class CoffeeMachine:
	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"
		
	class BrokenMachineExeption(Exception):
		def __init__(self):
			super().__init__("This machine went with God (foi com Deus)")

	def __init__(self):
		self.drinks_served = 0
		self.repaired = True

	def repair(self):
		self.repaired = True
		self.drinks_served = 0
		return "The Coffee machine is up and runnin'"

	def serve(self, hot_beverage):
		if self.drinks_served <= 10:
			drink_options = [hot_beverage, self.EmptyCup]
			drink = random.choice(drink_options)
			self.drinks_served += 1
			return drink()
		self.repaired = False
		raise self.BrokenMachineExeption

if __name__ == "__main__":
	drinks = [Coffee, Tea, Cappuccino, Chocolate]
	machine = CoffeeMachine()

	try:
		for random_drink in range(12):
			print(machine.serve(drinks[random_drink % 4]))
	except machine.BrokenMachineExeption as error:
		print(error)
	
	machine.repair()

	try:
		for random_drink in range(12):
			print(machine.serve(drinks[random_drink % 4]))
	except machine.BrokenMachineExeption as error:
		print(error)

class HotBeverage:
	name = "Hot Beverage"
	price = 0.30

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		return_beverage = ""
		return_beverage += \
			"Name : " + self.name + '\n' + \
			"Price : " + "{:.2f}".format(self.price) + '\n' + \
			"Description : " + self.description()
		return return_beverage

class Coffee(HotBeverage):
	name = "Coffee"
	price = 0.40

	def description(self):
		return "A coffee to stay awake"

class Tea(HotBeverage):
	name = "Tea"

class Chocolate(HotBeverage):
	name = "Chocolate"
	price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappucino(HotBeverage):
	name = "Cappucino"
	price = 0.45

	def description(self):
		return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
	drink = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappucino = Cappucino()
	print(drink, '\n\n', coffee, '\n\n', \
		tea, '\n\n', chocolate, '\n\n', cappucino)

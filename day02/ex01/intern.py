class Intern:
	class WorkException(Exception):
		def __init__(self, message):
			super().__init__(message)

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."
	
	def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
		self.name = name

	def __str__(self):
		return self.name

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return (Intern.Coffee())

if __name__ == "__main__":
	nameless = Intern()
	mark = Intern("Mark")
	print(nameless)
	print(mark)
	coffee = mark.make_coffee()
	print(coffee)
	try:
		nameless.work()
	except Exception as error:
		print(error)

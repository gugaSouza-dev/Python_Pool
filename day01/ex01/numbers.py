def	print_numbers():
	with open("numbers.txt", 'r') as file:
		numbers = file.read()
		splitted_numbers = numbers.split(',')
		for number in splitted_numbers:
			print(number.strip())

if __name__ == '__main__':
	print_numbers()

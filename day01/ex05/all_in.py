import sys

def	find_by_key(key_word, dict):
	for k, v in dict.items():
		if k == key_word:
			return v
	return False

def	find_by_value(key_word, dict):
	for k, v in dict.items():
		if v == key_word:
			return k
	return False

def error_check(args):
	if not len(sys.argv) == 2:
		sys.exit()
	for item in args:
		if item == '':
			sys.exit()

def	all_in():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	args = sys.argv[1].split(",")
	error_check(args)
	for item in args:
		arg = item.strip(" ").lower().title()
		if arg == '':
			continue
		state = find_by_key(find_by_key(arg, states), capital_cities)
		capital = find_by_value(find_by_value(arg, capital_cities), states)
		if state:
			print(state + " is the capital of " + arg)
			continue
		if capital:
			print(arg + " is the capital of " + capital)
			continue
		print(item.strip(" ") + " is neither a capital city nor a state")

if __name__ == '__main__':
	all_in()

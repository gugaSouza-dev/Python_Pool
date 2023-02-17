import sys

def	capital_exists(key_word, dict):
	for k, v in dict.items():
		if k == key_word:
			return v
	print("Unknown state")
	sys.exit()

def	capital_finder():
	if not len(sys.argv) == 2:
		sys.exit()
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
	state = sys.argv[1]
	capital = capital_exists(capital_exists(state, states), capital_cities)
	print(capital)

if __name__ == '__main__':
	capital_finder()

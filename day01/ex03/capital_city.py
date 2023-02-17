import sys

def	find_by_key(key_word, dict):
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
	capital = find_by_key(find_by_key(sys.argv[1], states), capital_cities)
	print(capital)

if __name__ == '__main__':
	capital_finder()

import sys

def	find_by_value(key_word, dict):
	for k, v in dict.items():
		if v == key_word:
			return k
	print("Unknown capital city")
	sys.exit()

def	state_finder():
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
	state_acronym = find_by_value(find_by_value(sys.argv[1], capital_cities), states)
	print(state_acronym)

if __name__ == '__main__':
	state_finder()

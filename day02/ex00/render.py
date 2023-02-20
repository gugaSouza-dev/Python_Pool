import sys, os
from settings import *

def	arg_error_check():
	if len(sys.argv) != 2:
		print("Error: invalid number of arguments. Try: `python3 render.py myCV.template`")
		sys.exit()
	arg = sys.argv[1]
	if not arg.endswith(".template"):
		print("Error: invalid file extention. Please use a `.template` file")
		sys.exit()
	if not os.path.isfile(arg):
		print("Error: file passed as argument does not exist.")
		sys.exit()


def	read_file(file):
	with open(file, "r") as infile_fd:
		return infile_fd.read().strip()


def	render(template):
	template_content = read_file(template)
	settings_content = open("settings.py", "r")
	for line in settings_content:
		key_value = line.split(" = ")
		if key_value[0].strip() != "":
			template_content = template_content.replace("{" + key_value[0] + "}",
				key_value[1].strip().strip("'"))	
	settings_content.close()
	with open(sys.argv[1].split(".")[0] + ".html", 'w') as html_file:
		html_file = html_file.write(template_content)


if __name__ == '__main__':
	arg_error_check()
	render(sys.argv[1])

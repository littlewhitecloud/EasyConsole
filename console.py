from os import getcwd, system

def cout(*text, end = ""):
	"Console out"
	for i in range(len(text)):
		print(text[i], end = end)
	if end != "\n":
		print("\n")
	
def cin(text = ""):
	return input(text)

__author__ = "XiaoBaiYun's Console"
__version__ = "1.0.2"

__about__ = """
%s %s
An easy program like a cmd(Command) program
Summary:
 Support program like cmd
	 Also can add you own rules
""" % (__author__, __version__)

_init = True # Control Console's init
_exit = False

if _init:
	system("title Console")
	cout(__author__, __version__, end = " ")

while not _exit:
	operator = input(getcwd() + '>')
	if operator == "exit": # Replace the original cmd exit
		_exit = True
	elif operator == "about": # Add a custom "about" function
		cout(__about__)
	# Add your own rules
	else: # Run operation in cmd
		system(operator)
		

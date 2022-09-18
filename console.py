# An easy console support cmd(Command).exe all function
# Summary :
# 	Support all cmd(Command).exe function
#	Can add own function

# Import
from os import system, getcwd

# Original
def cout(*text, end = ''):
	"Console Output"
	for i in range(len(text)):
		print(text[i], end = end)
		
	if end != '\n':
		print('\n')
		
def cin(text):
	"Console Input"
	return input(text)

# Extend
def example(*args):
	# Do something
	return 

# Variable
__version__ = "1.0.6"
__author__ = "Xiao_Bai_Yun"
__name__ = "Console"
__about__ = "%s %s %s" % (__author__, __name__, __version__)
__info__ = """
%s
# An easy console support cmd(Command).exe all function
# Summary :
# 	Support all cmd(Command).exe function
#	Can add own function
""" % (__about__)
_init = True
_exit = False

# Init
if _init:
	system("cls")
	system("title Console")
	cout(__about__)
	
# MainLoop
while not _exit:
	operator = cin("PS" + ' ' +  getcwd() + '>')
	if operator == "exit": # Replace cmd exit
		_exit = True
	elif operator == "info": # Add own func
		cout(__info__)
	elif operator == "about": # Add own func
		cout(__about__)
	else:
		try:
			system(operator)
		except KeyboardInterrupt:
			pass
		"EOFError"

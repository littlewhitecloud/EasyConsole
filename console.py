# An easy console support cmd(Command).exe all function
# Summary :
# 	Support all cmd(Command).exe function
#	Can add own function
#   Support UWP blur and acrylic
#   Smooth move~~~ (Doge
#   Blur:
#      Add Custom hex color
#      Use better blur
# Import
from os import system, getcwd
from runtime import *

# Variable
__version__ = "1.0.6"
__author__ = "Xiao_Bai_Yun"
__name__ = "Console"
__about__ = "%s %s %s" % (__author__, __name__, __version__)
__blur__ = True
__acrylic__ = True
__accent__ = 4
__info__ = """
%s
# An easy console support cmd(Command).exe all function
# Summary :
# 	Support all cmd(Command).exe function
#	Can add own function
""" % (__about__)
_init = True
_exit = False

if __blur__:
	from ctypes import windll
	from windowblur import blur
	hwnd = windll.user32.GetForegroundWindow()
	blur(hwnd = hwnd,Acrylic = __acrylic__, AccentState = __accent__) #Custom AccentState

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

# Console Runtime Functions

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

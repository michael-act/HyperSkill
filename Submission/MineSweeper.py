from random import shuffle

i = -1
def increment():
	global i
	i += 1
	return i

def arrangeGame(symbol):
	# Print the table game
	print('-------------------')
	symbol_m = [[symbol[increment()] for row in range(8)] for column in range(8)]
	for row in symbol_m:
		print('| ', end='')
		print(' '.join(str(cell) for cell in row), end='')
		print(' |')
	print('-------------------')

default = list('BBBBBBBBBB______________________________________________________')
shuffle(default)
arrangeGame(default)
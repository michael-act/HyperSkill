from random import shuffle
from time import process_time

class Increment:
	def __init__(self):
		self.i = -1

	def increment(self):
		self.i += 1
		return self.i

def arrangeGame(symbol):
	# Print the table game
	temp_symbol = symbol[::]

	print('-------------------')
	for row in symbol:
		print('| ', end='')
		print(' '.join(str(cell) for cell in row), end='')
		print(' |')
	print('-------------------')

def updateGame(coor):
	if [_ for _ in coor.strip() if _ in '012345678'] == []:
		print("You should enter numbers!")
		return False
	elif int(coor[0]) > 3 or int(coor[2]) > 4:
		print("Coordinates should be from 1 to 4!")
		return False
	else:
		out_line = 4 - int(coor[2])
		in_line = int(coor[0]) - 1
		value = ffruit[out_line][in_line]
		if [value for _ in bfruit if value in _] == [value, value]:
			print("This cell is occupied! Choose another one!")
			return False
		else:
			ffruit[out_line][in_line] = bfruit[out_line][in_line]
			return [out_line, in_line]

def checkWin(before, after):
	bvalue = ffruit[before[0]][before[1]]
	avalue = ffruit[after[0]][after[1]]
	if bvalue != avalue:
		arrangeGame(ffruit)
		print('Try Again!')
		ffruit[before[0]][before[1]] = '_'
		ffruit[after[0]][after[1]] = '_'
		arrangeGame(ffruit)
		return ''
	elif ffruit != bfruit and bvalue == avalue:
		arrangeGame(ffruit)
		return 'Good.'
	elif ffruit == bfruit and bvalue == avalue:
		arrangeGame(ffruit)
		return 'You win.'

bfruit = list('MMAASSPPKKRR')  #Mangga, Anggur, Semangka, Pisang, Kelengkeng, Rambutan
shuffle(bfruit)
ffruit_inc = Increment()
ffruit = [['_' for row in range(3)] for column in range(4)]
bfruit_inc = Increment()
bfruit = [[bfruit[bfruit_inc.increment()] for row in range(3)] for column in range(4)]

print('Tips: Match letter by letter to win the game!')
arrangeGame(ffruit)
start_time = process_time()
while True:
	act1 = updateGame(input("Enter the coordinates 1: > "))
	if act1:
		act2 = updateGame(input("Enter the coordinates 2: > "))
		if act2:
			check = checkWin(act1, act2)
			print(check)
			if check == 'You win.':
				break
			else:
				pass
		else:
			pass
	else:
		pass
end_time = process_time()
print(f'Spent Time: {end_time - start_time}')
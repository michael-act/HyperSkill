from random import shuffle
from time import perf_counter

class Increment:
	def __init__(self):
		self.i = -1

	def increment(self):
		self.i += 1
		return self.i

def setupGame(symbols):
	# Print the table game
	# print(f"  {'-' * (width * 2)}")
	for row in symbols:
		print(f'| ', end='')
		print(' '.join(str(cell) for cell in row), end='')
		print(' |')
	# print(f"  {'-' * (width * 2)}")

def helpGame():
	print("\nEx: Index of Table: ")
	print(".. | _ _ _ |")
	print("3  | _ _ _ |")
	print("2  | B _ _ |")
	print("1  | _ _ _ |")
	print("     1 2 .. ")
	print('Ex: Coordinates: 1 2\n')

def hintMine(symbols):
	def addMine(x=0, y=0):
		try:
			if (Id[0] + x) > -1 and (Id[1] + y) > -1:
				symbols[Id[0] + x][Id[1] + y] += 1
			else:
				pass
		except:
			pass

	minesId = [[o, i] for o in range(len(symbols)) 
			for i in range(len(symbols[o])) 
			if symbols[o][i] == 'B']

	for Id in minesId:
		# Add num to side of Bomb
		addMine(y=-1)
		addMine(y=1)

		# Add num to upside of Bomb
		addMine(x=-1)
		addMine(x=-1, y=-1)
		addMine(x=-1, y=1)

		# Add num to downside of Bomb
		addMine(x=1)
		addMine(x=1, y=-1)
		addMine(x=1, y=1)
	return symbols

def updateGame(coor):
	global match

	outId = height - int(coor[2])
	inId = int(coor[0]) - 1
	befSymbol = hideSymbols[outId][inId]
	hideSymbols[outId][inId] = realSymbols[outId][inId]
	match += 1
	return checkWin(befSymbol, outId, inId)

def getNeigbors(outId, inId):
	neighs = {}
	def addNeigh(x=0, y=0):
		if -1 < (outId + x) < 8 and -1 < (inId + y) < 8:
			neighs.update({f'{outId + x} {inId + y}': realSymbols[outId][inId]})
		else:
			pass

	# Add left side and right side neighbor
	addNeigh(y=-1)
	addNeigh(y=1)

	# Add upside neighbor
	addNeigh(x=-1)
	addNeigh(x=-1, y=-1)
	addNeigh(x=-1, y=1)

	# Add downside neighbor
	addNeigh(x=1)
	addNeigh(x=1, y=-1)
	addNeigh(x=1, y=1)

	return neighs

def recursiveNol(outId, inId):
	global match

	neighs = getNeigbors(outId, inId)
	nolId = [[int(_[0]), int(_[2])] for _ in neighs if neighs[_] == 0]
	for nol in nolId:
		tempNeighs = getNeigbors(nol[0], nol[1])
		tempNolId = [[int(_[0]), int(_[2])] for _ in tempNeighs 
					if tempNeighs[_] == 0]
		for temp in tempNolId:
			if temp not in nolId:
				nolId.append(temp)
			else:
				pass
		hideSymbols[nol[0]][nol[1]] = realSymbols[nol[0]][nol[1]]
		match += 1

def checkWin(bef, outId, inId):
	def whenWin():
		if match == (width * height - (mines - 1)):
			return True
		else:
			pass
	if bef != '_':
		return 'Pass'
	elif realSymbols[outId][inId] == 0:
		recursiveNol(outId, inId)
		if whenWin():
			return 'Win'
		else:
			return None
	elif realSymbols[outId][inId] == 'B':
		return False
	else:
		if whenWin():
			return 'Win'
		else:
			return None

# Determine size of MineSweeper Game
while True:
	width, height = int(input('Width size :> ')), int(input('Height size :> '))
	mines = int(input('Qty of mines: '))
	if (width and height > 3) and (mines < (width * height)):
		break
	else:
		print('Width or Height must greater than 3 and Mines must less than Width or Height')
		pass

# Arrange Default Table Value
symbols = []
for h in range(height):
	for w in range(width):
		symbols.append(0)
symbols[0:mines-1] = ['B' for _ in range(mines)]
shuffle(symbols)

# Backend Symbols
realInc = Increment()
realSymbols = hintMine([[symbols[realInc.increment()] 
			for row in range(width)] 
			for column in range(height)])

# Frontend Symbols
hideSymbols = [['_' for row in range(width)] 
			for column in range(height)]

# Playing a Game
helpGame()
setupGame(hideSymbols)
print()
start_time = perf_counter()
match = 0
while True:
	try:
		act = updateGame(input('Enter coordinates to open :> '))
		if act == None:
			setupGame(hideSymbols)
		elif act == 'Pass':
			print("This cell is occupied! Choose another one!")
		elif act == False:
			setupGame(realSymbols)
			print('Game over! Bye.')
			break
		elif act == 'Win':
			setupGame(realSymbols)
			print('Congrats! You won a game.')
			break
		else:
			pass
	except KeyboardInterrupt:
		print("\nThank you for playing! Bye.")
		break

end_time = perf_counter()
print(f'Spent Time: {round(end_time - start_time, 1)} Second')

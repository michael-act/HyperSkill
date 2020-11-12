# write your code here
def arrangeXO(symbol):
	global symbols

	symbols = symbol
	symbol_m = [[], [], []]
	temp_symbol = symbol[::]
	# Print the XO table
	print('---------')
	for i in range(3):
		print('|', end='')
		for _ in range(3):
			symbol_m[i].append(temp_symbol[0])
			print(f' {temp_symbol[0]}', end='')
			del temp_symbol[0]
		print(' |')
	print('---------')
	#print(check_win(symbol, symbol_m))

def check_win(symbol, symbol_m):
	in_line = [[symbol[_] for _ in range(0, 9, 4)], # Right Diagonal
				[symbol[_] for _ in range(2, 8, 2)], # Left Diagonal
				symbol_m[0], symbol_m[1], symbol_m[2], # Sideways
				[symbol[_] for _ in range(0, 9, 3)], # Decreased
				[symbol[_] for _ in range(1, 9, 3)], 
				[symbol[_] for _ in range(2, 9, 3)]]
	x_count = len([_ for _ in symbol if _ == 'X'])
	o_count = len([_ for _ in symbol if _ == 'O'])
	win = []
	match = 0
	for i in [['X'] * 3, ['O'] * 3]:
		for it in in_line:
			if i == it:
				win.append(i[0])
				match += 1
	if match == 1:
		return f'{win[0]} wins'
	elif match > 1 or abs(x_count - o_count) > 1:
		return 'Impossible'
	elif '_' in symbol:
		return 'Game not finished'
	elif '_' not in symbol:
		return 'Draw'
	else:
		pass

def updateXO(coor):
	symbol_set = {'1 3':symbols[0], '2 3':symbols[1], '3 3':symbols[2],
				'1 2':symbols[3], '2 2':symbols[4], '3 2':symbols[5],
				'1 1':symbols[6], '2 1':symbols[7], '3 1':symbols[8]}
	if [_ for _ in coor.strip() if _ in '012345678'] == []:
		print("You should enter numbers!")
	elif int(coor[0]) > 3 or int(coor[2]) > 3:
		print("Coordinates should be from 1 to 3!")
	elif symbol_set[coor] in 'XO':
		print("This cell is occupied! Choose another one!")
	else:
		symbol_set[coor] = 'X'
		arrangeXO(list(symbol_set.values()))
		return True

arrangeXO(list(input("Enter cells: > ")))
while True:
	if updateXO(input("Enter the coordinates: > ")) == True:
		break
	else:
		pass
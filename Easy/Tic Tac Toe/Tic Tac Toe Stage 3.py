# write your code here
def arrangeXO(symbol):
	symbol_m = [[], [], []]
	temp_symbol = symbol[::]
	print('---------')
	for i in range(3):
		print('|', end='')
		for _ in range(3):
			symbol_m[i].append(temp_symbol[0])
			print(f' {temp_symbol[0]}', end='')
			del temp_symbol[0]
		print(' |')
	print('---------')
	print(check_win(symbol, symbol_m))

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

arrangeXO(list(input("Enter cells: > ")))
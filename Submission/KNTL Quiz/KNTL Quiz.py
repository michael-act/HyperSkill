import sqlite3
from random import randint

def arrangeWord(word):
	print('----------')
	print(f'| {word} |')
	print('----------')

def initGame(status=False):
	global hideWord, realWord

	keyword = 'KENTEL'
	keyword = keyword.replace('E', 'O')
	data = readDB()
	realWord = data[0]
	wordDesc = data[1]
	hideWord = list(realWord)
	print(f'Question: {wordDesc}')
	for i in range(6):
		if realWord[i] != keyword[i]:
			hideWord[i] = '*'
	hideWord = ''.join(hideWord)
	arrangeWord(hideWord)

def checkGame(word):
	if word == realWord:
		print('Congrats! You got the word.')
		return True
	else:
		arrangeWord(hideWord)
		return False

def readDB():
	conn = sqlite3.connect('KNTLword.db')
	c = conn.cursor()
	c.execute(f'SELECT COUNT(*) FROM KNTLword')
	totalData = c.fetchall()[0][0]
	c.execute(f'SELECT word, word_desc FROM KNTLword WHERE word_id={randint(0, totalData - 1)}')
	data = c.fetchall()[0]
	return data

print("Type 'PASS' if you give up.")
initGame()
while True:
	answer = input('What the answer? > ').upper()
	if answer == 'PASS':
		print()
		initGame()
	elif checkGame(answer):
		break
	else:
		pass

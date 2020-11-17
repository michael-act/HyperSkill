import random
import sqlite3

def arrangeWord(word):
	print('----------')
	print(f'| {word} |')
	print('----------')

def initGame(word='', status=False):
	global hideWord

	hideWord = word
	if status:
		print('You Win!')
	else:
		letter = 'ABCDEFGHIJMPQRSUVWXYZ'
		for let in letter:
			hideWord = hideWord.replace(let, '*')
		arrangeWord(hideWord)

def updateGame(word):
	if word == realWord:
		initGame(word=hideWord, status=True)
		return True
	else:
		initGame(word=hideWord)
		return False

def readDB():
	conn = sqlite3.connect('KNTLword.db')
	c = conn.cursor()
	c.execute('SELECT word, word_desc FROM KNTLword')
	data = c.fetchall()
	return data

data = readDB()
setWord = data[random.randint(0, len(data))]
realWord = setWord[0]
wordDesc = setWord[1]
print(f'Question: {wordDesc}')
initGame(realWord)
while True:
	if updateGame(input('What the answer? > ')):
		break
	else:
		pass
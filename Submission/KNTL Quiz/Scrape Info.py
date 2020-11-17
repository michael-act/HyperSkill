import sqlite3
import requests
from bs4 import BeautifulSoup

def keyKNTL(word):
	keyword = 'KENTEL'
	keyword = keyword.replace('E', 'O')
	match = 0
	if len(word) == 6:
		for i in range(6):
			if keyword[i] == word[i]:
				match += 1
		if match > 2:
			return True
		else:
			return False
	else:
		return False

wordList = ['00-indonesian-wordlist.lst', 
			'02-crawls-2005-sort-alpha.lst', 
			'04-myspell2006-sort-alpha.lst', 
			'01-kbbi3-2001-sort-alpha.lst', 
			'03-indodict2008-sort-alpha.lst', 
			'05-ivanlanin2011-sort-alpha.lst']

for file in wordList:
	file = f'indonesian-wordlist/{file}'
	conndb = sqlite3.connect("KNTLword.db")
	openFile = open(file, encoding="ISO-8859-1")
	readFile = openFile.read().split("\n")
	for word in readFile:
		word = word.strip().upper()
		if keyKNTL(word) and len(word) == 6:
			page = requests.get(f'https://www.kamusbesar.com/{word}')
			soup = BeautifulSoup(page.content, 'html.parser')
			page_body = soup.findAll('span', {'class': 'word_description'})
			if page_body:
				info = str(page_body).split('</span>')[0]
				info = info[info.index('>')+1::].strip(';')
				conndb.execute(f"INSERT INTO KNTLword (word, word_desc) VALUES ('{word}', '{info}')")
				conndb.commit()
				print(f'{word}: Success')
			else:
				pass
		else:
			pass
import random
from string import ascii_lowercase

category = ['python', 'java', 'kotlin', 'javascript']
computer = random.choice(category)
hidden = list(len(computer) * "-")

print("H A N G M A N")
while True:
	menu = input('Type "play" to play the game, "exit" to quit: ')
	if menu == "play":
		pass
	elif menu == "exit":
		break
	else:
		continue

	counter = 8
	prev_letter = ""
	while counter > 0:
		print()
		print("".join(hidden))
		letter = input("Input a letter: ")
	
		if len(letter) > 1:
			print("You should input a single letter")
			continue
		elif letter not in ascii_lowercase:
			print("It is not an ASCII lowercase letter")
			continue
		elif (letter in hidden) or (letter in prev_letter) or (letter in hidden and times == 7):
			print("You already typed this letter")
			continue
		elif letter in set(computer):
			where = 0 
			for i in range(computer.count(letter)):
				where = computer.index(letter, 0 + where)
				hidden[where] = letter
				where += where + 1
			if "-" not in hidden:
				print()
				print("".join(hidden))
				print(f"You guessed the word {computer}!")
				print("You survived!")
				break
		else:
			counter -= 1
			print("No such letter in the word")
		prev_letter = prev_letter + letter
	else:
		print("You are hanged!")
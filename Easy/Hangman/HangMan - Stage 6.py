import random

category = ['python', 'java', 'kotlin', 'javascript']
computer = random.choice(category)
hidden = list(len(computer) * "-")

print("H A N G M A N")
counter = 8
while counter > 0:
	print()
	print("".join(hidden))
	letter = input("Input a letter: ")

	if (letter in hidden) or (letter in hidden and times == 7):
		counter -= 1
		print("No improvements")
	elif letter in set(computer):
		where = 0 
		for i in range(computer.count(letter)):
			where = computer.index(letter, 0 + where)
			hidden[where] = letter
			where += where + 1
		if "-" not in hidden:
			print()
			print("".join(hidden))
			print("You guessed the word!")
			print("You survived!")
			break
	else:
		counter -= 1
		print("No such letter in the word")
	print(counter)
else:
	print("You are hanged!")
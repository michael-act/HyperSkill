import random

category = ['python', 'java', 'kotlin', 'javascript']
computer = random.choice(category)
hidden = list(len(computer) * "-")

print("H A N G M A N\n")
for times in range(8):
	print("".join(hidden))
	letter = input("Input a letter: ")
	if letter in set(computer):
		count = computer.count(letter)
		if letter in set(hidden):
			print("No improvements")
			pass
		elif count > 1:
			where = 0 
			for i in range(count):
				where = computer.index(letter, 0 + where)
				hidden[where] = letter
				where += where + 1
		else:
			where = computer.index(letter)
			hidden[where] = letter
	elif "-" not in hidden:
		break
	else:
		print("No such letter in the word")
	print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")

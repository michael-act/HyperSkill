# Write your code here

class NewRequest:
	def __init__(self):
		self.stock = {"water":400, "milk":540, "beans":120, "cups":9, "money":550}
	def action(self, action, order=None, dictAdd={}):
		if action == 'buy':
			OptStock('-', self, order=order)
		elif action == 'fill':
			OptStock('+', self, dictAdd=dictAdd)
		elif action == 'take':
			print(f"\nI gave you ${self.stock['money']}")
			self.stock['money'] -= self.stock['money']
		elif action == 'remaining':
			print(f"\nThe coffee machine has:")
			print(f"{self.stock['water']} of water")
			print(f"{self.stock['milk']} of milk")
			print(f"{self.stock['beans']} of coffee beans")
			print(f"{self.stock['cups']} of disposable cups")
			print(f"${self.stock['money']} of money")

class OptStock:
	def __init__(self, opt, obj_stock, order=None, dictAdd={}):
		self.stock_keys = list(obj_stock.stock.keys())
		self.stock_values = list(obj_stock.stock.values())
		self.recipes_dict = {
		'1': {'water': 250, 'milk':0, 'beans': 16, 'cups': 1, 'money': 4}, 
		'2': {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'money': 7}, 
		'3': {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'money': 6}}

		if opt == '-':
			if OptStock.check_can(self, list(self.recipes_dict[order].values())) == False:
				return
			else:
				OptStock.reduce(self, order, obj_stock)
		elif opt == '+':
			OptStock.add(obj_stock, dictAdd=dictAdd)
		else:
			pass

	def check_can(self, listMin):
		for i in range(5):
			if self.stock_values[i] < listMin[i]:
				print(f"Sorry, not enough {self.stock_keys[self.stock_values.index(self.stock_values[i])]}!")
				return False
		else:
			print("I have enough resources, making you a coffee!")
		
	def reduce(self, order, obj_stock):
		obj_stock.stock = {
		"water":obj_stock.stock['water'] - self.recipes_dict[order]['water'], 
		"milk":obj_stock.stock['milk'] - self.recipes_dict[order]['milk'], 
		"beans":obj_stock.stock['beans'] - self.recipes_dict[order]['beans'], 
		"cups":obj_stock.stock['cups'] - self.recipes_dict[order]['cups'], 
		"money":obj_stock.stock['money'] + self.recipes_dict[order]['money']}

	def add(obj_stock, dictAdd):
		obj_stock.stock = {
		"water":obj_stock.stock['water'] + dictAdd['water'], 
		"milk":obj_stock.stock['milk'] + dictAdd['milk'], 
		"beans":obj_stock.stock['beans'] + dictAdd['beans'], 
		"cups":obj_stock.stock['cups'] + dictAdd['cups'], 
		"money":obj_stock.stock['money'] + dictAdd['money']}	

CoffeeMachine = NewRequest()
while True:
	action = input("Write action (buy, fill, take, remaining, exit):\n")

	if action == "buy":
		buy_opt = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
		if buy_opt == 'back':
			print()
			continue
		CoffeeMachine.action(action='buy', order=buy_opt)
	elif action == "fill":
		waterAdd = int(input("Write how many ml of water do you want to add:\n"))
		milkAdd = int(input("Write how many ml of milk do you want to add:\n"))
		beansAdd = int(input("Write how many grams of coffee beans do you want to add:\n"))
		cupsAdd = int(input("Write how many disposable cups of coffee do you want to add:\n"))		
		CoffeeMachine.action(action='fill', dictAdd={
			'water':waterAdd, 
			'milk':milkAdd, 
			'beans':beansAdd, 
			'cups':cupsAdd, 
			'money':0})
	elif action == "take":
		CoffeeMachine.action(action='take')
	elif action == "remaining":
		CoffeeMachine.action(action='remaining')
	elif action == "exit":
		break
	else:
		pass
	print()
# Write your code here
stock = {"water":400, "milk":540, "beans":120, "cups":9, "money":550}

def opt_stock(waterMin=0, milkMin=0, beansMin=0, cupsMin=0, moneyAdd=0):
	if check_can([waterMin, milkMin, beansMin, cupsMin, moneyAdd]) == False:
		return
	else:
		global stock_values_backup
		stock_values_backup = {"waterAdd":waterMin, "milkAdd":milkMin, "beansAdd":beansMin, "cupsAdd":cupsMin, "moneyMin":moneyAdd}
		stock['water'] -= waterMin
		stock['milk'] -= milkMin
		stock['beans'] -= beansMin
		stock['cups'] -= cupsMin
		stock['money'] += moneyAdd

def check_can(listMin):
	for i in range(5):
		if stock_values[i] < listMin[i]:
			print(f"Sorry, not enough {stock_keys[stock_values.index(stock_values[i])]}!")
			return False
	else:
		print("I have enough resources, making you a coffee!")

def fill(waterAdd=0, milkAdd=0, beansAdd=0, cupsAdd=0, moneyMin=0):
	stock['water'] += waterAdd
	stock['milk'] += milkAdd
	stock['beans'] += beansAdd
	stock['cups'] += cupsAdd
	stock['money'] += moneyMin

def main():
	while True:
		global stock_keys, stock_values

		stock_keys = list(stock.keys())
		stock_values = list(stock.values())
		opt = input("Write action (buy, fill, take, remaining, exit):\n")
		if opt == "buy":
			buy_opt = int(input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
			if buy_opt == 1:
				opt_stock(waterMin=250, beansMin=16, cupsMin=1, moneyAdd=4)
			elif buy_opt == 2:
				opt_stock(waterMin=350, milkMin=75, beansMin=20, cupsMin=1, moneyAdd=7)
			elif buy_opt == 3:
				opt_stock(waterMin=200, milkMin=100, beansMin=12, cupsMin=1, moneyAdd=6)
			else:
				pass
		elif opt == "fill":
			waterAdd = int(input("Write how many ml of water do you want to add:\n"))
			milkAdd = int(input("Write how many ml of milk do you want to add:\n"))
			beansAdd = int(input("Write how many grams of coffee beans do you want to add:\n"))
			cupsAdd = int(input("Write how many disposable cups of coffee do you want to add:\n"))
			fill(waterAdd, milkAdd, beansAdd, cupsAdd)
		elif opt == "back":
			fill(stock_values_backup['waterAdd'], 
				stock_values_backup['milkAdd'], 
				stock_values_backup['beansAdd'], 
				stock_values_backup['cupsAdd'],
				stock_values_backup['moneyMin'])
		elif opt == "take":
			print(f"I gave you ${stock['money']}\n")
			stock['money'] -= stock['money']
		elif opt == "remaining":
			print(f"\nThe coffee machine has:")
			print(f"{stock['water']} of water")
			print(f"{stock['milk']} of milk")
			print(f"{stock['beans']} of coffee beans")
			print(f"{stock['cups']} of disposable cups")
			print(f"${stock['money']} of money")
		elif opt == "exit":
			break
		else:
			pass
		print()

main()
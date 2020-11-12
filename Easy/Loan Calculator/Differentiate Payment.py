# write your code here

from sys import argv, exit
import string
import math
import argparse

if len(argv) < 5 or len(argv) > 5:
	print("Incorrect parameters")
	exit()

def diff_payment(P, n, I):
	i = monthly_rate(I)

	add_all = 0
	for month in range(1, round(I) + 1):
		hasil = P / n + i * (P - (P * (month - 1) / n))
		add_all += math.ceil(hasil)
		print(f"Month {month}: paid out {math.ceil(hasil)}")
	print(f" \nOverpayment = {math.ceil(add_all - P)}")

def annuity_pay(P, n, i):
	i = monthly_rate(i)

	hasil = P * ((i * pow(1+i, n)) / (pow(1+i, n) - 1) )
	return math.ceil(hasil)

def credit_principal(A, n, i):
	i = monthly_rate(i)

	hasil = A / ((i * pow(1+i, n)) / (pow(1+i, n) - 1))
	return int(hasil)

def num_month(P, A, i):
	i = monthly_rate(i)
	hasil = A / (A - i * P)
	hasil_log = math.ceil(math.log(hasil, 1 + i))

	return hasil_log

def monthly_rate(i):
	hasil = (i / 100) / (12 * (100 / 100))
	return hasil

def not_ascii(value):
	string_ = string.ascii_letters + string.punctuation.replace('.', '')
	for letter in string_:
		if letter in value:
			print("Incorrect parameters")
			raise parse.exit()
	if value == '':
		print("Incorrect parameters")
		raise parse.exit()
	return value

def check_positive(value):
	not_ascii(value)
	if "." in value:
		ivalue = float(value)
		if ivalue <= 0.0:
			print("Incorrect parameters")
			raise parse.exit()
	else:
		ivalue = int(value)
		if ivalue <= 0:
			print("Incorrect parameters")
			parse.exit()
	return ivalue

parse = argparse.ArgumentParser()
parse.add_argument("--type", dest="type_")
parse.add_argument("--principal", type=check_positive, dest="principal")
parse.add_argument("--payment", type=check_positive, dest="payment")
parse.add_argument("--periods", type=check_positive, dest="periods")
parse.add_argument("--interest", type=check_positive,dest="interest")
args = parse.parse_args()

diff = [args.principal, args.periods, args.interest]
annuity_1 = [args.principal, args.periods, args.interest]
annuity_2 = [args.payment, args.periods, args.interest]
annuity_3 = [args.principal, args.payment, args.interest]

if args.type_ == "diff" and None not in diff:
	diff_payment(annuity_1[0], annuity_1[1], annuity_1[2])

elif args.type_ == "annuity" and None not in annuity_1:
	ann_pay = annuity_pay(annuity_1[0], annuity_1[1], annuity_1[2])
	print(f"Your annuity payment = {ann_pay}!")
	print(f"Overpayment = {math.ceil(ann_pay * annuity_1[1] - annuity_1[0])}")

elif args.type_ == "annuity" and None not in annuity_2:
	credit_p = credit_principal(annuity_2[0], annuity_2[1], annuity_2[2])
	print(f"Your credit principal = {credit_p}!")
	print(f"Overpayment = {math.ceil(annuity_2[0] * annuity_2[1] - credit_p)}")

elif args.type_ == "annuity" and None not in annuity_3:
	sum_month = num_month(annuity_3[0], annuity_3[1], annuity_3[2])

	if sum_month <= 12:
		print(f"You need {sum_month} months to repay this credit!" 
			if sum_month > 1
			else f"You need {sum_month} month to repay this credit!")

	elif sum_month > 12:
		year = sum_month // 12
		month = abs(year * 12 - sum_month)

		if year > 1 < month:
			print(f"You need {year} years and {month} months to repay this credit!")
		if year > 1 == month:
			print(f"You need {year} years and {month} month to repay this credit!")
		elif year == 1 < month:
			print(f"You need {year} year and {month} months to repay this credit!")
		elif year > 1 > month:
			print(f"You need {year} years to repay this credit!")
	print(f"Overpayment = {math.ceil(annuity_3[1] * sum_month - annuity_3[0])}")

else:
	print("Incorrect parameters")
	parse.exit()

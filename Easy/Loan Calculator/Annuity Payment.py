# write your code here
import math

print('What do you want to calculate?')
print('type "n" - for count of months, ')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal: ')
option = input()

def annuity_pay(P, n, i):
    i = monthly_rate(i)

    hasil = P * ((i * pow(1+i, n)) / (pow(1+i, n) - 1) )
    return math.ceil(hasil)

def credit_principal(A, n, i):
    i = monthly_rate(i)

    hasil = A / ((i * pow(1+i, n)) / (pow(1+i, n) - 1))
    return round(hasil)

def num_month(P, A, i):
    i = monthly_rate(i)

    hasil = A / (A - i * P)
    hasil_log = math.log(hasil, 1 + i)
    return math.ceil(hasil_log)

def monthly_rate(i):
    hasil = (i / 100) / (12 * (100 / 100))
    return hasil

if option == "n":
    credit_p = float(input("Enter credit principal: \n"))
    monthly_p = float(input("Enter monthly payment: \n"))
    credit_i = float(input("Enter credit interest: \n"))
    sum_month = num_month(credit_p, monthly_p, credit_i)

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
            
elif option == "a":
    credit_p = float(input("Enter credit principal: \n"))
    count_p = float(input("Enter count of periods: \n"))
    credit_i = float(input("Enter credit interest: \n"))

    ann_pay = annuity_pay(credit_p, count_p, credit_i)
    print(f"Your annuity payment = {ann_pay}!")

elif option == "p":
    monthly_p = float(input("Enter monthly payment: \n"))
    count_p = float(input("Enter count of periods: \n"))
    credit_i = float(input("Enter credit interest: \n"))

    credit_p = credit_principal(monthly_p, count_p, credit_i)
    print(f"Your credit principal = {credit_p}!")

else:
    pass

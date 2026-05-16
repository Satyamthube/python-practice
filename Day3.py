# practice questions for conditions if & else
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"The down payment will be: {down_payment}")


#even and odd
number=int(input('enter the number '))
if number % 2 == 0:
    print("number is even")
else:
    print('number is odd')

#positive or negative
number=int(input('enter the number '))
if number>=0:
    print("number is positive")
else:
    print('number is negative')

#task completion
traning_hours=float(input('enter traning hrs '))
if traning_hours>=2:
    print('good progress')
else:
    print('need improvement')
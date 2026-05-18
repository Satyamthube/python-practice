#Q1 Odd or Even
number=int(input('Enter number '))
if number % 2 == 0:
    print('number is even')
else:
    print('number is odd')

#Q2 Multiplication table
number=int(input('enter number '))
for i in range (1,11):
   print(number,'X',i,'=',number*i)

#Sum of number
numbers=[]

for i in range (3):
    number=int(input('enter number = '))
    numbers.append(number)

    total=sum(numbers)
    print(total)

#positive, negative or zero
number=float(input('enter number '))
if number>0:
    print('positive')
elif number<0:
    print('negative')
else:
    print('zero')

# greating player
def greet_player(name):
    print(f"{name} keep pushing forward")

    greet_player("satyam")

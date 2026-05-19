try:
    age = int(input("Enter age: "))
    print(age)
except:
    print("Invalid Input")

#Q practice question

try:
    sum1=int(input("enter number 1 "))
    sum2=int(input("enter number 2 "))
    total=sum1+sum2
    print(total)
except:
    print('invalid input')


try:
    num = float(input("Enter a number: "))
    print("Square =", num * num)
except:
    print("Invalid number")
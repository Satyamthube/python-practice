#Q1
try:
    num1 = int(input('enter number = '))
    num2 = int(input('enter number = '))
    num3 = int(input('enter number = '))

    if num1 > num2 and num1 > num3 :
        print("Largest Number = ",num1)
    elif num2 > num1 and num2 > num3:
        print("Largest Number = ",num2)
    else:
        print("Largest Number = ",num3)

except:
    print("invalid input")

#Q2
total = 0

for i in range (1,101):
    if i % 2 == 0:
        total += i

print("total of all even numbers will be : ", total)

#Q3
marks= [33,34,66,99,98]
average = sum(marks)/len(marks)
print(average)

#Q4
student={
    "name" : "satyaa",
    "age" : 20,
    "sport" : "baseball"
}
key = input("Enter key: ")
print("Value:", student.get(key, "Key not found"))

#Q5   
try:
    age = int(input("Enter age: "))
    print(age)
except:
    print("Invalid Input")
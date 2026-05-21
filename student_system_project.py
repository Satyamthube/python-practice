student_details = {}
student_details["name"] = input("enter student name: ")

mark1 = int(input("enter marks "))
mark2 = int(input("enter marks "))

average = (mark1+mark2) / 2

if average >= 90:
    grade="A"
elif average >= 75:
    grade="B"
elif average >= 50:
    grade="C"
else:
    grade="fail"

print("\nstudent details")
print('student name = ', student_details["name"])
print('average = ',average)
print('grade = ',grade)
marks = []

for i in range(3):
    mark = int(input("Enter marks: "))
    marks.append(mark)

print("Student Marks:", marks)

total = sum(marks)

print("Total Marks =", total)

average = total / len(marks)

print("Average =", average)
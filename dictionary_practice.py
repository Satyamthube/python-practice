student= {
    "name" : "satyam",
    "age":20,
    "sport" : "baseball"
}

print(student["name"])

student["city"] = "Rahuri"

for key, value in student.items():
    print(key, ":", value)

#practice Q1
my_self= {
    "name":"satyam",
    "age" : 20,
    "sport":"baseball",
    "goal":"money"
}
for key, value in my_self.items():
    print(value)

#practice Q2
sub_marks = {
    "math": 80,
    "science": 90,
    "english": 85
}
total = sum(sub_marks.values())
print("Total Marks:", total)
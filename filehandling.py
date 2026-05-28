#OPENING A FILE
file = open("data.txt", "w")


#WRITING TO FILE
file.write("Hello Satyam")


#CLOSE FILE
file.close()


#example 
file = open("notes.txt", "w")
file.write("Day 6 completed")
file.close()


#READ FILE
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


#APPEND MODE
file = open("notes.txt", "a")
file.write("\nKeep improving daily")
file.close()


#practice example 1
#Ask user for name. Save it in file.
name = input("Enter your name: ")
with open("output.txt", "w") as file:
    file.write(name)


#practice example 2
#Ask user for daily workout hours. Save into file.
workout_hours=int(input('enter workout hours '))
with open("output.txt", "w") as file:
    file.write(int(workout_hours))
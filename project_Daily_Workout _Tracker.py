#FEATURES
#Program should:
# 1.Ask workout details 2.Save into file 3.Read previous workout logs 4.Show total sessions

workout = input("Enter workout name: ")
hours = input("Enter workout hours: ")

with open("workout_log.txt", "a") as file:
    file.write(f"{workout} - {hours} hours\n")

print("\nPrevious Workout Logs:")
with open("workout_log.txt", "r") as file:
    logs = file.readlines()
    for log in logs:
        print(log.strip())

print("\nTotal Sessions:", len(logs))

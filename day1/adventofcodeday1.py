elves = []
greatest_calories = 0
calorie_sum = 0

with open("./day1/input.txt", "r") as input:
    input_lines = input.readlines()

def addElvesCalories(calorie_sum):
    for line in input_lines:
        if line.rstrip("\n") == "":
            elves.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(line)

def getGreatestCalories(greatest_calories):
    for calorie in elves:
        if calorie > greatest_calories:
            greatest_calories = calorie
    print(greatest_calories)

def getTopThreeElvesCalories():
    elves.sort()
    elves.reverse()
    print(sum(elves[:3]))

addElvesCalories(calorie_sum)
print("First challenge outcome: ")
getGreatestCalories(greatest_calories)
print("Second challenge outcome: ")
getTopThreeElvesCalories()
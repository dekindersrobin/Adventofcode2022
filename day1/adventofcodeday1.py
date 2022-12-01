elves = []
greatest_calories = 0
calorie_sum = 0

with open("input.txt", "r") as input:
    input_lines = input.readlines()

for line in input_lines:
    if line.rstrip("\n") == "":
        elves.append(calorie_sum)
        calorie_sum = 0
    else:
        calorie_sum += int(line)

for calorie in elves:
    if calorie > greatest_calories:
        greatest_calories = calorie

print(greatest_calories)

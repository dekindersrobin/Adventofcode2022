A, X, B, Y, C, Z = 1, 1, 2, 2, 3, 3
inputs = []
score = 0

with open("./day2/input.txt", "r") as input:
    input_lines = input.readlines()

for line in input_lines:
    inputs.append(line.split())

for battle in inputs:
    if battle[0] == "A" and battle[1] == "X":
        score += X + 3
    elif battle[0] == "A" and battle[1] == "Y":
        score += Y + 6
    elif battle[0] == "A" and battle[1] == "Z":
        score += Z + 0
    elif battle[0] == "B" and battle[1] == "X":
        score += X + 0
    elif battle[0] == "B" and battle[1] == "Y":
        score += Y + 3
    elif battle[0] == "B" and battle[1] == "Z":
        score += Z + 6
    elif battle[0] == "C" and battle[1] == "X":
        score += X + 6
    elif battle[0] == "C" and battle[1] == "Y":
        score += Y + 0
    elif battle[0] == "C" and battle[1] == "Z":
        score += Z + 3
    print(battle[0] + " VS " + battle[1] + " : " + str(score))
    

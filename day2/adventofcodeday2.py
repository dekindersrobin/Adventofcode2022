A, X, B, Y, C, Z = 1, 0, 2, 3, 3, 6
inputs = []
score = 0

with open("./day2/input.txt", "r") as input:
    input_lines = input.readlines()

for line in input_lines:
    inputs.append(line.split())

for battle in inputs:
    if battle[0] == "A" and battle[1] == "X":
        score += C + X
    elif battle[0] == "A" and battle[1] == "Y":
        score += A + Y
    elif battle[0] == "A" and battle[1] == "Z":
        score += B + Z
    elif battle[0] == "B" and battle[1] == "X":
        score += A + X
    elif battle[0] == "B" and battle[1] == "Y":
        score += B + Y
    elif battle[0] == "B" and battle[1] == "Z":
        score += C + Z
    elif battle[0] == "C" and battle[1] == "X":
        score += B + X
    elif battle[0] == "C" and battle[1] == "Y":
        score += C + Y
    elif battle[0] == "C" and battle[1] == "Z":
        score += A + Z
    print(battle[0] + " VS " + battle[1] + " : " + str(score))
    

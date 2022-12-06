amount = 0

with open("./day4/input.txt", "r") as input:
    input_lines = input.readlines()

for input in input_lines:
    elve1 = input.split(",")[0]
    elve2 = input.split(",")[1]
    elve1p1 = int(elve1.split("-")[0])
    elve1p2 = int(elve1.split("-")[1])
    elve2p1 = int(elve2.split("-")[0])
    elve2p2 = int(elve2.split("-")[1].replace("\n", ""))

    seperate_elves = [elve1p1, elve1p2, elve2p1, elve2p2]

    biggest_number = max(seperate_elves)
    smallest_number = min(seperate_elves)

    if (elve2p1 == biggest_number or elve2p2 == biggest_number) and (elve2p1 == smallest_number or elve2p2 == smallest_number):
        amount += 1
    elif (elve1p1 == biggest_number or elve1p2 == biggest_number) and (elve1p1 == smallest_number or elve1p2 == smallest_number):
        amount += 1
    elif ((elve1p1 <= elve2p1) or (elve1p2 <= elve2p2)) and ((elve1p2 >= elve2p1) or (elve1p1 >= elve2p2)):
        amount += 1
    elif ((elve2p1 <= elve1p1) or (elve2p2 <= elve1p2)) and ((elve2p2 >= elve1p1) or (elve2p1 >= elve1p2)):
        amount += 1



    print(elve1)
    print(elve2)

    print(amount)
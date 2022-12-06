alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
common_chars = []
sum = 0
group = []
i = 1

with open("./day3/input.txt", "r") as input:
    input_lines = input.readlines()

for line in input_lines:
    group.append(line.replace("\n", ""))

    if i == 3:
        first_line = group[0]
        second_line = group[1]
        third_line = group[2]

        common_chars += list(set(first_line)&set(second_line)&set(third_line))

        i = 0
        group.clear()
    i += 1

print(common_chars)

for char in common_chars:
    sum += alphabet.index(char) + 1

print(sum)
    

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
common_chars = []
sum = 0

with open("./day3/input.txt", "r") as input:
    input_lines = input.readlines()

for line in input_lines:
    first_part_of_line = line[0:len(line)//2]
    second_part_of_line = line[len(line)//2:len(line)]

    print(first_part_of_line)
    print(second_part_of_line)
    common_chars += list(set(first_part_of_line)&set(second_part_of_line))

    print(common_chars)

for char in common_chars:
    sum += alphabet.index(char) + 1

print(sum)
    

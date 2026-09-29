# 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3
with open("numbers.txt") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
    print(number_1 + number_2)

# 4
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        total += int(line)
print(total)

# Odd Numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Countdown from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print Number of Stars
number_of_stars = int(input("How many stars do you want? "))
print("*" * number_of_stars)

# Print lines of increasing stars
number_of_stars = int(input("How many stars do you want? "))
for i in range(number_of_stars):
    print("*" * (i + 1))

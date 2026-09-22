# EG Output
# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92
DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))

total = 0

for item in range(number_of_items):
    total += float(input("Price of item: "))

if total > 100:
    total *= (1-DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total:.2f}")

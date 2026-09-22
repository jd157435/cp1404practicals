"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_RATE_LOW = 0.1
BONUS_RATE_HIGH = 0.15

sales = float(input("Enter sales (-1 to exit): $"))
while sales >= 0:
    if sales < 1000:
        bonus_amount = sales * BONUS_RATE_LOW
    else:
        bonus_amount = sales * BONUS_RATE_HIGH

    print(f"Bonus: {bonus_amount}")
    print("----------------------")
    sales = float(input("Enter sales (-1 to exit): $"))
print("Thanks for using this program.")



"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(f"User score {user_score:.1f} is {user_result}")
    if user_result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_result(score: float) -> str:
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


if __name__ == '__main__':
    main()

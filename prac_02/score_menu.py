"""
CP1404/CP5632 - Practical
Program to display score menu
"""

from score import determine_result
from math import floor

MENU = """
(G)et a valid score (must be 0-100)
(P)rint result
(S)how stars
(Q)uit
"""


def main() -> None:
    user_score = get_valid_score()
    print(MENU)
    choice = input(":")
    while choice != "Q":
        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_result(user_score)}")
        elif choice == "S":
            print_stars(user_score)
        else:
            print("Invalid Option")
        print(MENU)
        choice = input(":")
    print("Farewell")


def get_valid_score() -> float:
    user_score = float(input("Enter score: "))
    while user_score < 0 or user_score > 100:
        print("Invalid Score. Must be between 0 and 100.")
        user_score = float(input("Enter score: "))
    return user_score


def print_stars(user_score: float) -> None:
    print("*" * floor(user_score))


main()

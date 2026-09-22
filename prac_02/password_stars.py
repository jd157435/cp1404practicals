"""Print number of stars equal to length of password"""


def main():
    minimum_length = 10

    password = get_password(minimum_length)
    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password(minimum_length: int) -> str:
    password = input("Password:")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long.")
        password = input("Password:")
    return password


main()

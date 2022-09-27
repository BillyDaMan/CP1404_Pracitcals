MIN_LENGTH = 5


def main():
    """Refactor password check program to use functions"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Displays the password"""
    print("Your password is", len(password) * "*")


def get_password():
    """Checks if password reaches minimum length"""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"The password does not meet the minimum length of {MIN_LENGTH}")
        password = input("Enter password: ")
    return password


main()

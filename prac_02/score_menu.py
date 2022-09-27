MENU = "(G) - Get valid score\n(R) - Print results\n(S) - Print stars\n(Q) - Quit"


def main():
    score = 0
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Score: ", 0, 100)
        elif choice == "R":
            category = determine_score_category(score)
            print(f"Your score is {score}, making your category: {category}")
        elif choice == "S":
            display_star_score(score)
        else:
            print("Invalid Option")
        print(MENU)
        choice = input("> ").upper()
    print("Goodbye")


def get_valid_number(prompt, low, high):
    """Determine if number is valid or not"""
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid score")
        number = int(input(prompt))
    return number


def determine_score_category(score):
    """Determine the score category"""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def display_star_score(score):
    """Displays score as *"""
    print(f"Your score displayed as '*'\n{'*' * score}")


main()

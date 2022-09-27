"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Scores"""
    score = float(input("Enter score: "))
    category = determine_score_category(score)
    print(f"Your score is {score}, making your category: {category}")
    score = random.randint(0, 100)
    category = determine_score_category(score)
    print(f"Your random score is {score}, making your category: {category}")


def determine_score_category(score):
    """Determine the score category"""
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score < 101:
        return "Excellent"
    else:
        return "Invalid score"


main()

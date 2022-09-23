"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
if score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
elif score < 101:
    print("Excellent")
else:
    print("Invalid score")

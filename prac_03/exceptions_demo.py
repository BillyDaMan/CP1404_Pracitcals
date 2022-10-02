"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    If anything but an integer is inputted

2. When will a ZeroDivisionError occur?
    If 0 is inputted in the denominator (anything / 0 will give the error)

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Add a while loop for the second input so that it won't proceed until a number
    higher then 0 is inputted
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
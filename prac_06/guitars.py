"""
CP1404 Practical - Guitars
Estimate: 25 minutes
Actual:   35 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Add and displays guitar's name, year and cost."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for number, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(number, guitar, vintage_string))
    else:
        print("Done")


main()

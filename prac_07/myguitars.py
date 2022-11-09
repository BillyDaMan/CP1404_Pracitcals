"""
CP1404 Practical - My Guitars
Estimate: 30 minutes
Actual:   24 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Read file for guitars and display them"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar}", file=out_file)
    out_file.close()


main()

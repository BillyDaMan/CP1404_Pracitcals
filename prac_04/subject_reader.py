"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    records = get_records()
    display_records(records)


def get_records():
    """Read data from file formatted like: subject,lecturer,number of students."""
    records = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        records.append(parts)
        print("----------")
    input_file.close()
    return records


def display_records(records):
    """Displays the subjects"""
    for record in records:
        print("{} is taught by {:12} and has {:3} students".format(*record))


main()

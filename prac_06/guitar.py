"""
CP1404 Practical - Guitar
Estimate: 35 minutes
Actual:   31 minutes
(This time includes the guitar_test program)
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 100


class Guitar:
    """Represents a guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        """wip"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Displays the guitar information."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Gets the current age of the guitar from the current"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines whether the guitar is vintage or not based off the age"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year

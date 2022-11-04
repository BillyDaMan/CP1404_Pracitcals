"""CP1404 Practical - Guitar Test"""

from prac_06.guitar import Guitar


def run_tests():
    """Tests for the Guitar class."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
    other = Guitar("Another Guitar", 2013, 600.5)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 9. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()

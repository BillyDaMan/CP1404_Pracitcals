"""
CP1404 Practical - Programming Languages
Estimate: 30 minutes
Actual:   22 minutes
"""


class ProgrammingLanguage:
    """Represents a language object."""

    def __init__(self, field, typing, reflection, year):
        """Creates a programming language from the values given."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a programming language representation as a string"""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic or not."""
        return self.typing == "Dynamic"

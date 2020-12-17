"""
CP1404/CP5632 Practical
Programming Language class.
"""


class ProgrammingLanguage():
    """Display the information about a programming language"""

    def __init__(self, name, typing, reflection, year):
        self.typing = typing.lower()
        self.reflection = reflection
        self.year = year
        self.name = name

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Check whether the typing is dynamic or not"""
        if self.typing == 'dynamic':
            return True
        else:
            return False

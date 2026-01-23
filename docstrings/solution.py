"""
Problem: Docstrings
URL: https://neetcode.io/problems/python-docstrings/question
Language: python

Solution by NeetCode GitHub Pusher
"""

        """Return the sound the pet makes based on its type."""
    def make_sound(self) -> str:
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# Don't change the following code
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)


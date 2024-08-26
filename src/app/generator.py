"""
Password generation logic.
"""

import random
import string

class PasswordGenerator:
    """
    A class to generate random passwords based on specified criteria.
    """

    @staticmethod
    def generate(length=12, use_digits=True, use_special=True) -> str:
        """
        Generate a random password.

        :param length: Length of the password (default is 12).
        :param use_digits: Include digits in the password (default is True).
        :param use_special: Include special characters in the password (default is True).
        :return: A randomly generated password as a string.
        """
        characters = string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        return ''.join(random.choice(characters) for _ in range(length))

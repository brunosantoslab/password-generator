"""
Unit tests for the PasswordGenerator and PasswordGeneratorGUI classes.
"""

import sys
import os
import unittest

# Ensure the src directory is in the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app.generator import PasswordGenerator
from app.gui import PasswordGeneratorGUI

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_default(self):
        password = PasswordGenerator.generate()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isdigit() for char in password))
        
        # Use the full set of special characters defined in PasswordGenerator
        special_characters = set("!@#$%^&*()")
        self.assertTrue(any(char in special_characters for char in password), "Password does not contain any special characters")

    def test_generate_without_digits(self):
        password = PasswordGenerator.generate(use_digits=False)
        self.assertFalse(any(char.isdigit() for char in password))

    def test_generate_without_special(self):
        password = PasswordGenerator.generate(use_special=False)
        self.assertFalse(any(char in '!@#$%^&*()' for char in password))

    def test_generate_custom_length(self):
        password = PasswordGenerator.generate(length=20)
        self.assertEqual(len(password), 20)

    def test_generate_min_length(self):
        password = PasswordGenerator.generate(length=PasswordGeneratorGUI.MIN_PASSWORD_LENGTH)
        self.assertEqual(len(password), PasswordGeneratorGUI.MIN_PASSWORD_LENGTH)

    def test_generate_max_length(self):
        password = PasswordGenerator.generate(length=PasswordGeneratorGUI.MAX_PASSWORD_LENGTH)
        self.assertEqual(len(password), PasswordGeneratorGUI.MAX_PASSWORD_LENGTH)

    def test_generate_too_short(self):
        with self.assertRaises(ValueError):
            gui = PasswordGeneratorGUI()
            gui.validate_length(str(PasswordGeneratorGUI.MIN_PASSWORD_LENGTH - 1))

    def test_generate_too_long(self):
        with self.assertRaises(ValueError):
            gui = PasswordGeneratorGUI()
            gui.validate_length(str(PasswordGeneratorGUI.MAX_PASSWORD_LENGTH + 1))

    def test_generate_empty_length(self):
        with self.assertRaises(ValueError):
            gui = PasswordGeneratorGUI()
            gui.validate_length("")

    def test_generate_whitespace_length(self):
        with self.assertRaises(ValueError):
            gui = PasswordGeneratorGUI()
            gui.validate_length("   ")


if __name__ == "__main__":
    unittest.main()
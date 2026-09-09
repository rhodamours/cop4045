import unittest

from p5_Desamours_Rhodney import (
    caesar_cipher,
    caesar_decipher,
    letter_frequency
)


class TestCaesarCipher(unittest.TestCase):

    def test_cipher_basic_shift(self):
        self.assertEqual(
            caesar_cipher("abc", 3),
            "def"
        )

    def test_cipher_wraparound(self):
        self.assertEqual(
            caesar_cipher("xyz", 3),
            "abc"
        )

    def test_cipher_preserves_case(self):
        self.assertEqual(
            caesar_cipher("Hello", 3),
            "Khoor"
        )

    def test_cipher_preserves_spaces(self):
        self.assertEqual(
            caesar_cipher("Hello World", 3),
            "Khoor Zruog"
        )

    def test_decipher_basic(self):
        self.assertEqual(
            caesar_decipher("Khoor", 3),
            "Hello"
        )

    def test_decipher_wraparound(self):
        self.assertEqual(
            caesar_decipher("abc", 3),
            "xyz"
        )

    def test_cipher_decipher_round_trip(self):
        message = "Python Is Fun"
        shift = 7

        encrypted = caesar_cipher(message, shift)
        decrypted = caesar_decipher(encrypted, shift)

        self.assertEqual(decrypted, message)


class TestLetterFrequency(unittest.TestCase):

    def test_frequency_counts_letters(self):
        expected = {
            'h': 1,
            'e': 1,
            'l': 2,
            'o': 1
        }

        result = letter_frequency("Hello")

        for letter, count in expected.items():
            self.assertEqual(result[letter], count)

    def test_frequency_ignores_case(self):
        result = letter_frequency("AaA")

        self.assertEqual(result['a'], 3)

    def test_frequency_ignores_non_letters(self):
        result = letter_frequency("A! A? 123")

        self.assertEqual(result['a'], 2)

    def test_frequency_empty_string(self):
        result = letter_frequency("")

        total = sum(result.values())
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
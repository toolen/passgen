"""This file contains application constants."""
import string

MIN_LENGTH = 4
MAX_LENGTH = 254
DEFAULT_LENGTH = 6
ASCII_LOWERCASE = string.ascii_lowercase
ASCII_UPPERCASE = string.ascii_uppercase
ASCII_LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATION = string.punctuation
ALPHABET = ASCII_LETTERS + DIGITS + PUNCTUATION
REQUIRED_SEQUENCES = (
    ASCII_LOWERCASE,
    ASCII_UPPERCASE,
    DIGITS,
    PUNCTUATION,
)

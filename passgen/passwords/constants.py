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
ALPHABET_WO_PUNCTUATION = ASCII_LETTERS + DIGITS
REQUIRED_SEQUENCES = (
    ASCII_LOWERCASE,
    ASCII_UPPERCASE,
    DIGITS,
    PUNCTUATION,
)
REQUIRED_SEQUENCES_WO_PUNCTUATION = (
    ASCII_LOWERCASE,
    ASCII_UPPERCASE,
    DIGITS,
)

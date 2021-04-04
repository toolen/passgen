"""This file contains service methods to generate passwords."""
import secrets

from .constants import (
    ALPHABET,
    ALPHABET_WO_PUNCTUATION,
    MAX_LENGTH,
    MIN_LENGTH,
    REQUIRED_SEQUENCES,
    REQUIRED_SEQUENCES_WO_PUNCTUATION,
)


def validate_length(length: int) -> None:
    """
    Validate password length.

    :param int length: password length
    :return: None
    :raises AssertionError: if length is invalid
    """
    if length is None:
        raise AssertionError("Must be not None")

    if type(length) is not int:
        raise AssertionError("Must be an integer")

    if length < MIN_LENGTH:
        raise AssertionError(f"Less than the minimum length {MIN_LENGTH}")

    if length > MAX_LENGTH:
        raise AssertionError(f"Greater than the maximum length {MAX_LENGTH}")


def get_password(length: int, exclude_punctuation: bool = False) -> str:
    """
    Return password.

    :param int length: password length
    :param bool exclude_punctuation: generate password without special chars
    :return: password
    :rtype: str
    """
    validate_length(length)

    alphabet = ALPHABET_WO_PUNCTUATION if exclude_punctuation else ALPHABET
    sequences = (
        REQUIRED_SEQUENCES_WO_PUNCTUATION if exclude_punctuation else REQUIRED_SEQUENCES
    )

    password = []
    for _ in range(0, length):
        password.append(secrets.choice(alphabet))

    idx_list = list([x for x in range(0, length)])

    for sequence in sequences:
        idx = secrets.choice(idx_list)
        idx_list.remove(idx)
        password[idx] = secrets.choice(sequence)

    return "".join(password)

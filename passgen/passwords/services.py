import secrets

from .constants import MIN_LENGTH, MAX_LENGTH, ALPHABET, REQUIRED_SEQUENCES


def validate_length(length):
    if length is None:
        raise AssertionError('Must be not None')

    if type(length) is not int:
        raise AssertionError('Must be an integer')

    if length < MIN_LENGTH:
        raise AssertionError(f'Less than the minimum length {MIN_LENGTH}.')

    if length > MAX_LENGTH:
        raise AssertionError(f'Greater than the maximum length {MAX_LENGTH}')


def get_password(length):
    validate_length(length)

    password = []
    for _ in range(0, length):
        password.append(secrets.choice(ALPHABET))

    idx_list = list([x for x in range(0, length)])
    for sequence in REQUIRED_SEQUENCES:
        idx = secrets.choice(idx_list)
        idx_list.remove(idx)
        password[idx] = secrets.choice(sequence)

    return ''.join(password)

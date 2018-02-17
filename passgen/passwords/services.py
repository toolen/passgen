import secrets

from .constants import MIN_LENGTH, MAX_LENGTH, ALPHABET, REQUIRED_SEQUENCES


def get_password(length):
    assert length is not None, 'Must be not None'
    assert type(length) is int, 'Must be an integer'
    assert length >= MIN_LENGTH, 'Less than the minimum length {0}.'.format(MIN_LENGTH)
    assert length <= MAX_LENGTH, 'Greater than the maximum length {0}'.format(MAX_LENGTH)

    password = []
    for _ in range(0, length):
        password.append(secrets.choice(ALPHABET))

    idx_list = list([x for x in range(0, length)])
    for sequence in REQUIRED_SEQUENCES:
        idx = secrets.choice(idx_list)
        idx_list.remove(idx)
        password[idx] = secrets.choice(sequence)

    return ''.join(password)

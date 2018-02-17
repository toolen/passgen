import pytest

from passgen.passwords.constants import MAX_LENGTH, MIN_LENGTH
from passgen.passwords.services import get_password


def test_get_password():
    length = int(MAX_LENGTH - MIN_LENGTH / 2)
    password = get_password(length)

    assert type(password) is str
    assert len(password) == length


@pytest.mark.parametrize('invalid_length, expected_exception', [
    (None, AssertionError,),
    ('test', AssertionError,),
    (MIN_LENGTH - 1, AssertionError),
    (MAX_LENGTH + 1, AssertionError),
])
def test_get_password_w_various_invalid_length(invalid_length, expected_exception):
    with pytest.raises(expected_exception):
        get_password(invalid_length)


def test_get_password_w_various_valid_length():
    for length in (MIN_LENGTH, int(MAX_LENGTH - MIN_LENGTH / 2), MAX_LENGTH,):
        password = get_password(length)

        assert len(password) == length

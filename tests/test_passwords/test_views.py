import pytest

from passgen.passwords.constants import (
    DEFAULT_LENGTH,
    MAX_LENGTH,
    MIN_LENGTH,
    PUNCTUATION,
)
from passgen.utils import BOOL_TRUE_STRINGS


async def test_get_password_wo_length_param(client):
    url = client.app.router["passwords"].url_for()
    result = await client.get(url)

    assert result.status == 200

    data = await result.json()
    password = data.get("password")

    assert type(password) is str
    assert len(password) == DEFAULT_LENGTH


@pytest.mark.parametrize(
    "length, expected_status_code",
    [
        ("test", 400),
        (MIN_LENGTH - 1, 400),
        (MIN_LENGTH, 200),
        (int(MAX_LENGTH - MIN_LENGTH / 2), 200),
        (MAX_LENGTH, 200),
        (MAX_LENGTH + 1, 400),
    ],
)
async def test_get_password_w_various_length(client, length, expected_status_code):
    url = client.app.router["passwords"].url_for().with_query({"length": length})
    result = await client.get(url)

    assert result.status == expected_status_code


@pytest.mark.parametrize(
    "param_value",
    BOOL_TRUE_STRINGS,
)
async def test_get_password_w_exclude_punctuation_param(client, param_value):
    url = (
        client.app.router["passwords"]
        .url_for()
        .with_query({"exclude_punctuation": param_value})
    )
    result = await client.get(url)

    assert result.status == 200

    data = await result.json()
    password = data.get("password")

    for char in PUNCTUATION:
        assert char not in password

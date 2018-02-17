import pytest

from passgen.passwords.constants import MIN_LENGTH, MAX_LENGTH, DEFAULT_LENGTH


def test_get_password_wo_length_param(client, password_resource_url):
    result = client.simulate_get(password_resource_url)

    assert result.status_code == 200
    password = result.json
    assert type(password) is str
    assert len(password) == DEFAULT_LENGTH


@pytest.mark.parametrize('length, expected_status_code', [
    ('test', 400),
    (MIN_LENGTH - 1, 400),
    (MIN_LENGTH, 200),
    (int(MAX_LENGTH - MIN_LENGTH / 2), 200),
    (MAX_LENGTH, 200),
    (MAX_LENGTH + 1, 400),
])
def test_get_password_w_various_length(client, password_resource_url, length, expected_status_code):
    qs = 'length={0}'.format(length)
    result = client.simulate_get(password_resource_url, query_string=qs)

    assert result.status_code == expected_status_code

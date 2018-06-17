import uuid

import pytest

from passgen.utils import get_bool_env


@pytest.mark.parametrize('key, default, expected', [
    (str(uuid.uuid4()), None, False),
    (str(uuid.uuid4()), True, True),
    ('TEST_ENV_VAR', None, True),
])
def test_get_bool_env(monkeypatch, key, default, expected):
    monkeypatch.setenv('TEST_ENV_VAR', 'True')
    value = get_bool_env(key, default)
    assert value == expected

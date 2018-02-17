import pytest
from falcon import testing

from passgen.app import application


@pytest.fixture()
def client():
    return testing.TestClient(application)


@pytest.fixture()
def password_resource_url():
    return '/passgen/api/v1/passwords'

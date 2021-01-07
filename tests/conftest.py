import pytest

from passgen.app import create_app


@pytest.fixture
async def client(aiohttp_client):
    app = await create_app()
    return await aiohttp_client(app)

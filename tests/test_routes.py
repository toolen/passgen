async def test_health(client):
    url = (
        client.app.router["health"]
        .url_for()
    )
    result = await client.get(url)

    assert result.status == 200

    data = await result.json()
    assert data.get("health") == "ok"

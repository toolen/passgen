"""This file contains routes methods."""
from aiohttp import web
from aiohttp.web_response import Response

from passgen.passwords.views import passwords


async def health(request: web.Request) -> Response:
    """
    Return healthcheck response.

    :return: Response
    """
    return web.json_response({"health": "ok"})


def init_routes(app: web.Application) -> None:
    """
    Initialize application routes.

    :param web.Application app: instance of application
    :return: None
    """
    app.router.add_route("GET", "/api/v1/passwords", passwords, name="passwords")
    app.router.add_route("GET", "/api/v1/health", health, name="health")

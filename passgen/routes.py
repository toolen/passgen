"""This file contains routes methods."""
from aiohttp import web

from passgen.passwords.views import passwords


def init_routes(app: web.Application) -> None:
    """
    Initialize application routes.

    :param web.Application app: instance of application
    :return: None
    """
    app.router.add_route("GET", "/api/v1/passwords", passwords, name="passwords")

"""This file contains routes methods."""
from aiohttp import web
from aiohttp_cors import CorsConfig

from passgen.passwords.views import passwords


def init_routes_with_cors(app: web.Application, cors: CorsConfig) -> None:
    """
    Initialize application routes with CORS.

    :param web.Application app: instance of application
    :param CorsConfig cors: cors configuration
    :return: None
    """
    resource = cors.add(app.router.add_resource("/api/v1/passwords", name="passwords"))
    cors.add(resource.add_route("GET", passwords))


def init_routes(app: web.Application) -> None:
    """
    Initialize application routes.

    :param web.Application app: instance of application
    :return: None
    """
    add_route = app.router.add_route
    add_route("GET", "/api/v1/passwords", passwords, name="passwords")

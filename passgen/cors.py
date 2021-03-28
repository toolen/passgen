"""This file contains CORS methods."""
import aiohttp_cors
from aiohttp import web
from aiohttp_cors import ResourceOptions

default_headers = (
    'Host',
    'User-Agent',
    'Accept',
    'Accept-Language',
    'Accept-Encoding',
    'Access-Control-Request-Method',
    'Access-Control-Request-Headers',
    'Origin',
    'Connection',
    'Pragma',
    'Cache-Control',
    'Content-Type',
)

default_methods = (
    "GET",
    "OPTIONS",
)


def init_cors(app: web.Application) -> None:
    """
    Initialize application with CORS.

    :param web.Application app: instance of application
    :return: instance of application with initialized CORS
    :rtype: web.Application
    """
    cors_origin = app["settings"]["cors_origin"]
    cors = aiohttp_cors.setup(
        app,
        defaults={
            cors_origin: ResourceOptions(
                allow_headers=default_headers, allow_methods=default_methods
            )
        },
    )
    for route in list(app.router.routes()):
        cors.add(route)

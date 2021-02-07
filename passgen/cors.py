import aiohttp_cors
from aiohttp import web
from aiohttp_cors import CorsConfig, ResourceOptions

default_headers = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

default_methods = (
    "GET",
    "OPTIONS",
)


def init_cors(app: web.Application) -> CorsConfig:
    cors_origin = app["settings"]["cors_origin"]
    cors = aiohttp_cors.setup(
        app,
        defaults={
            cors_origin: ResourceOptions(
                allow_headers=default_headers, allow_methods=default_methods
            )
        },
    )

    return cors

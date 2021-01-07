import aiohttp_cors
from aiohttp import web
from aiohttp_cors import CorsConfig, ResourceOptions

default_headers = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

default_methods = (
    # 'DELETE',
    'GET',
    'OPTIONS',
    # 'PATCH',
    # 'POST',
    # 'PUT',
)


def init_cors(app: web.Application) -> CorsConfig:
    cors = aiohttp_cors.setup(app, defaults={
        '*': ResourceOptions(
            allow_headers=default_headers,
            allow_methods=default_methods
        )
    })

    return cors

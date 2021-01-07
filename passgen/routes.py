from aiohttp import web
from aiohttp_cors import CorsConfig

from passgen.passwords.views import passwords


def init_routes_with_cors(app: web.Application, cors: CorsConfig) -> None:
    resource = cors.add(app.router.add_resource('/api/v1/passwords', name='passwords'))
    cors.add(resource.add_route('GET', passwords))


def init_routes(app: web.Application) -> None:
    add_route = app.router.add_route
    add_route('GET', '/api/v1/passwords', passwords, name='passwords')

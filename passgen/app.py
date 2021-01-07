from aiohttp import web
from aiohttp.abc import Application

from passgen.cors import init_cors
from passgen.routes import init_routes, init_routes_with_cors
from passgen.settings import CORS_ENABLED


async def create_app() -> web.Application:
    app: Application = web.Application()

    if CORS_ENABLED:
        cors = init_cors(app)
        init_routes_with_cors(app, cors)
    else:
        init_routes(app)

    return app

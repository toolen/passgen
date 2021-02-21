from typing import Dict, Optional

from aiohttp import web

from passgen.cors import init_cors
from passgen.routes import init_routes
from passgen.settings import init_settings


async def create_app(settings: Optional[Dict[str, str]] = None) -> web.Application:
    app: web.Application = web.Application()
    app = init_settings(app, settings)
    init_routes(app)
    if app["settings"]["cors_enabled"]:
        init_cors(app)

    return app

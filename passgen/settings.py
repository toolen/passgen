from typing import Dict, Optional

from aiohttp import web

from .utils import get_bool_env, get_string_env


def init_settings(
    app: web.Application, settings: Optional[Dict[str, str]]
) -> web.Application:
    app['settings'] = {
        'cors_enabled': get_bool_env('PASSGEN_CORS_ENABLED', True),
        'cors_origin': get_string_env('PASSGEN_CORS_ORIGIN', '*'),
    }
    if settings:
        app['settings'].update(settings)
    return app

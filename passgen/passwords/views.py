"""This file contains application views."""
from aiohttp import web
from aiohttp.web_response import Response

from .constants import DEFAULT_LENGTH
from .services import get_password


async def passwords(request: web.Request) -> Response:
    """
    Return response with generated password.

    :param web.Request request: object contains all information
    about incoming HTTP request
    :return: Response with generated password
    """
    try:
        length_str = request.rel_url.query.get("length", DEFAULT_LENGTH)
        length = int(length_str)
        password = get_password(length)
        return web.json_response({"password": password})
    except ValueError:
        return web.json_response(
            {
                "title": "Invalid parameter",
                "description": 'The "length" parameter is invalid.',
            },
            status=400,
        )
    except AssertionError as exc:
        return web.json_response(
            {
                "title": "Invalid parameter",
                "description": f'The "length" parameter is invalid. {str(exc)}.',
            },
            status=400,
        )

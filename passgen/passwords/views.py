"""This file contains application views."""
from typing import Final

import multidict
from aiohttp import web
from aiohttp.web_response import Response

from passgen.utils import BOOL_TRUE_STRINGS

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
        query_params: Final[multidict.MultiDict[str]] = request.rel_url.query

        raw_length: str = query_params.get("length", str(DEFAULT_LENGTH))
        length: int = int(raw_length)

        raw_exclude_punctuation: str = query_params.get("exclude_punctuation", "")
        exclude_punctuation: bool = raw_exclude_punctuation in BOOL_TRUE_STRINGS

        password = get_password(length, exclude_punctuation)

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

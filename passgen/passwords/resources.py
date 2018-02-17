import json

import falcon

from .constants import DEFAULT_LENGTH
from .services import get_password


class PasswordsResource(object):

    @staticmethod
    def on_get(req, resp):

        try:
            length_str = req.params.get('length', DEFAULT_LENGTH)
            length = int(length_str)
            password = get_password(length)
        except ValueError:
            raise falcon.HTTPInvalidParam('Unable convert to integer value', 'length')
        except AssertionError as exc:
            raise falcon.HTTPInvalidParam(str(exc), 'length')

        resp.body = json.dumps(password, ensure_ascii=False)
        resp.status = falcon.HTTP_200

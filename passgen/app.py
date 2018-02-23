import falcon

from .cors import cors
from .passwords.resources import PasswordsResource

application = falcon.API(middleware=[cors.middleware])

passwords = PasswordsResource()
application.add_route('/passgen/api/v1/passwords', passwords)

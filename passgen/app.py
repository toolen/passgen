import falcon
from falcon_cors import CORS

from passgen.passwords.resources import PasswordsResource

cors = CORS(allow_all_origins=True)

application = falcon.API(middleware=[cors.middleware])

passwords = PasswordsResource()
application.add_route('/passgen/api/v1/passwords', passwords)

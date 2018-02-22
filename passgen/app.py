import falcon
from falcon_cors import CORS

from passgen.passwords.resources import PasswordsResource

cors = CORS(allow_all_origins=True, allow_all_headers=True,
            allow_methods_list=['OPTIONS', 'GET'])

application = falcon.API(middleware=[cors.middleware])

passwords = PasswordsResource()
application.add_route('/passgen/api/v1/passwords', passwords)

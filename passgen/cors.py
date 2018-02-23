from falcon_cors import CORS

default_headers = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

default_methods = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

cors = CORS(allow_all_origins=True,
            allow_headers_list=default_headers,
            allow_methods_list=default_methods)

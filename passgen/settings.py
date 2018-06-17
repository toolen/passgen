from .utils import get_bool_env

CORS_ENABLED = get_bool_env('PASSGEN_CORS_ENABLED', True)

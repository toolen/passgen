import os


def get_bool_env(key, default=None):
    bool_true_strings = ('true', 'on', 'ok', 'y', 'yes', '1',)
    value = os.getenv(key, default)
    is_string = isinstance(value, str)
    return (value.lower() in bool_true_strings) if is_string else bool(value)

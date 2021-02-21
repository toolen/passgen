import os
from typing import Union


def get_bool_env(key: str, default: bool = False) -> bool:
    bool_true_strings = (
        "true",
        "on",
        "ok",
        "y",
        "yes",
        "1",
    )
    value: Union[str, None] = os.getenv(key)
    if value is not None:
        return value.lower() in bool_true_strings
    else:
        return bool(default)


def get_string_env(key: str, default: str = '') -> str:
    return os.getenv(key, default)

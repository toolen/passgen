"""This file contains utils methods."""
import os
from typing import Union


def get_bool_env(key: str, default: bool = False) -> bool:
    """
    Return boolean value from environment variable.

    :param str key: name of environment variable
    :param bool default: default value if environment variable not exists or empty
    :return: boolean value from environment variable
    :rtype: bool
    """
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
    """
    Return string value from environment variable.

    :param str key: name of environment variable
    :param str default: default value if environment variable not exists or empty
    :return: string value from environment variable
    :rtype: bool
    """
    return os.getenv(key, default)

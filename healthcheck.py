#!/usr/bin/env python
"""Custom healthcheck script."""
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def main() -> None:
    """
    Entrypoint.

    :return: None
    """
    try:
        response = urlopen('http://127.0.0.1:8080/api/v1/health')  # nosec
        if response.code == 200:
            sys.exit(0)
        else:
            sys.exit(1)
    except HTTPError:
        sys.exit(1)
    except URLError:
        sys.exit(1)


if __name__ == '__main__':
    main()

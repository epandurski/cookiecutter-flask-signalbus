#!/usr/bin/env python

try:
    from dotenv import load_dotenv
except ImportError:
    pass
else:
    load_dotenv()

from {{cookiecutter.app_slug}} import create_app  # noqa
from {{cookiecutter.app_slug}}.extensions import broker  # noqa
import {{cookiecutter.app_slug}}.actors  # noqa

app = create_app()
broker.set_default()

if __name__ == '__main__':
    import sys
    print(
        "This script is intended to be imported by Dramatiq's CLI tools.\n"
        "\n"
        "Usage: dramatiq tasks:BROKER_NAME\n"
    )
    sys.exit(1)

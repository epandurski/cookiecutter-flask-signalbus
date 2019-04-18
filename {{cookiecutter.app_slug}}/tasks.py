#!/usr/bin/env python

from {{cookiecutter.app_slug}} import create_app
from {{cookiecutter.app_slug}}.extensions import broker

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

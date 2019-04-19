#!/usr/bin/env python

import logging.config
from contextlib import suppress

# Configure logging if a "logging.conf" file is present.
with suppress(FileNotFoundError), open('logging.conf') as f:
    logging.config.fileConfig(f)

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

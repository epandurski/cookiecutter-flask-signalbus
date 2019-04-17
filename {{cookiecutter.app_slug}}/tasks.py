#!/usr/bin/env python

from {{cookiecutter.app_slug}} import create_app
from {{cookiecutter.app_slug}}.extensions import broker

app = create_app()
broker.set_default()

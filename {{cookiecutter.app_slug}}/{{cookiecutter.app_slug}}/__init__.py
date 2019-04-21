__version__ = '0.1.0'

import os
import logging
import logging.config
from flask_env import MetaFlaskEnv

logging_conffile = os.environ.get('APP_LOGGING_CONFIG_FILE')
if logging_conffile:
    logging.config.fileConfig(logging_conffile)
else:
    logging.basicConfig(level=logging.WARNING)


class Configuration(metaclass=MetaFlaskEnv):
    SECRET_KEY = 'dummy-secret'
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_POOL_SIZE = None
    SQLALCHEMY_POOL_TIMEOUT = None
    SQLALCHEMY_POOL_RECYCLE = None
    SQLALCHEMY_MAX_OVERFLOW = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DRAMATIQ_BROKER_CLASS = 'RabbitmqBroker'
    DRAMATIQ_BROKER_URL = 'amqp://guest:guest@localhost:5672'
    RABBITMQ_EVENT_EXCHANGE = ''


def create_app(config_dict={}):
    from flask import Flask
    from .extensions import db, migrate, broker

    app = Flask(__name__)
    app.config.from_object(Configuration)
    app.config.from_mapping(config_dict)
    db.init_app(app)
    migrate.init_app(app, db)
    broker.init_app(app)
    return app

import click
from flask.cli import with_appcontext


@click.group('{{cookiecutter.app_slug}}')
def {{cookiecutter.app_slug}}():
    """Perform {{cookiecutter.app_name}} specific operations."""


@{{cookiecutter.app_slug}}.command()
@with_appcontext
@click.argument('queue_name')
def subscribe(queue_name):  # pragma: no cover
    """Subscribe a queue for the observed events and messages.

    QUEUE_NAME specifies the name of the queue.

    """

    from .extensions import broker, DRAMATIQ_EXCHANGE_NAME
    from . import actors  # noqa

    channel = broker.channel
    channel.exchange_declare(DRAMATIQ_EXCHANGE_NAME)
    click.echo(f'Declared "{DRAMATIQ_EXCHANGE_NAME}" direct exchange.')

    if environ.get('APP_USE_LOAD_BALANCING_EXCHANGE', ''):
        bind = channel.exchange_bind
        unbind = channel.exchange_unbind
    else:
        bind = channel.queue_bind
        unbind = channel.queue_unbind
    bind(queue_name, DRAMATIQ_EXCHANGE_NAME, queue_name)
    click.echo(f'Subscribed "{queue_name}" to "{DRAMATIQ_EXCHANGE_NAME}.{queue_name}".')

    for actor in [broker.get_actor(actor_name) for actor_name in broker.get_declared_actors()]:
        if 'event_subscription' in actor.options:
            routing_key = f'events.{actor.actor_name}'
            if actor.options['event_subscription']:
                bind(queue_name, DRAMATIQ_EXCHANGE_NAME, routing_key)
                click.echo(f'Subscribed "{queue_name}" to "{DRAMATIQ_EXCHANGE_NAME}.{routing_key}".')
            else:
                unbind(queue_name, DRAMATIQ_EXCHANGE_NAME, routing_key)
                click.echo(f'Unsubscribed "{queue_name}" from "{DRAMATIQ_EXCHANGE_NAME}.{routing_key}".')

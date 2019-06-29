import click
from flask.cli import with_appcontext


@click.group('{{cookiecutter.app_slug}}')
def {{cookiecutter.app_slug}}():
    """Perform {{cookiecutter.app_name}} specific operations."""


# Define your CLI commands here. For example:
#
#     @{{cookiecutter.app_slug}}.command()
#     @with_appcontext
#     @click.option('-o', '--option', type=str, help='An option description')
#     def do_something(processes):
#         """Does something."""

{{cookiecutter.app_name}}
{{'=' * cookiecutter.app_name|length}}

{{cookiecutter.description}}


Setting up a development environment
------------------------------------

To create an `.env` file with reasonable defalut values, run this command::

  $ cp env.development .env

Then install a RabbitMQ server on `localhost` and either create a new
user, or allow the existing `guest` user to connect from other hosts
(by default, only local connections are allowed for `guest`).
